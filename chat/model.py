import logging
from threading import Semaphore
from typing import Dict, List

import sqlpuzzle

from .db import db_connection


class User:
    def __init__(self, ip: str, name: str) -> None:
        self.ip = ip
        self.name = name

    def __str__(self) -> str:
        return 'User {}'.format(self.name)

    def __repr__(self) -> str:
        return '<User ip={s.ip} name={s.name}>'.format(s=self)

    def __eq__(self, obj) -> bool:
        return self.ip == obj.ip and self.name == obj.name


class Messages:
    def __init__(self, db_config: dict) -> None:
        self._db_config = db_config
        self._lock = Semaphore()
        self._messages = []  # type: List[Dict]

    def __iter__(self):
        with self._lock:
            messages = list(self._messages)
        for message in messages:
            yield message

    def add(self, message: dict) -> None:
        logging.info('Trying to add message %r', message)
        with self._lock:
            self._messages.insert(0, {
                'user_name': message['user_name'],
                'message': message['message'],
            })
        logging.debug('Message %r added', message)

    def load(self) -> None:
        with db_connection(self._db_config) as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS messages (user_name TEXT, message TEXT);')

            sql = sqlpuzzle.select('user_name', 'message').from_('messages')
            cursor.execute(str(sql))
            self._messages = [{
                'user_name': message[0],
                'message': message[1],
            } for message in cursor.fetchall()]

    def save(self) -> None:
        with db_connection(self._db_config) as cursor:
            sql = sqlpuzzle.delete_from('messages').allow_delete_all()
            cursor.execute(str(sql))

            if self._messages:
                sql = sqlpuzzle.insert_into('messages')
                for message in self._messages:
                    sql.values(message)
                cursor.execute(str(sql))
