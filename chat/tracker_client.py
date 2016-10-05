from json.decoder import JSONDecodeError
import logging

import requests

from .config import ConfigMixin
from .exceptions import ChatException
from .model import User
from .retry import retry


class TrackerClient(ConfigMixin):
    def __init__(self, http_client=requests, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._http_client = http_client

    @retry(3)
    def get_users(self):
        r = self._http_client.get('{}/users'.format(self.tracker_url), timeout=self.tracker_timeout)
        if r.status_code != 200:
            raise ChatException('')
        try:
            users = r.json()
        except JSONDecodeError:
            return ()
        logging.debug('Logged users: %r', users)
        return [User(user['ip'], user['name']) for user in users]

    @retry(5)
    def join(self):
        r = self._http_client.post('{}/join'.format(self.tracker_url), json={'name': self.user_name}, timeout=self.tracker_timeout)
        if r.status_code != 200:
            raise ChatException('')
        logging.info('User %s successfully joined', self.user_name)
