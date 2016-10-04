import logging
from threading import Semaphore


class User:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name

    def __str__(self):
        return 'User {}'.format(self.name)

    def __repr__(self):
        return '<User ip={s.ip} name={s.name}>'.format(s=self)


class Messages:
    def __init__(self):
        self._lock = Semaphore()
        self._messages = []

    def __iter__(self):
        with self._lock:
            messages = list(self._messages)
        for message in messages:
            yield message

    def add(self, message):
        logging.info('Trying to add message %r', message)
        with self._lock:
            self._messages.insert(0, message)
        logging.debug('Message %r added', message)
