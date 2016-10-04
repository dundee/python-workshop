from json.decoder import JSONDecodeError

import requests

from .exceptions import ChatException
from .retry import retry


class TrackerClient:
    def __init__(self, config):
        self._config = config

    @property
    def url(self):
        return self._config['tracker']['url']

    @property
    def _user_name(self):
        return self._config['user']['name']

    @property
    def _timeout(self):
        return float(self._config['tracker']['timeout'])

    @retry
    def get_users(self):
        r = requests.get('{}/users'.format(self.url), timeout=self._timeout)
        if r.status_code != 200:
            raise ChatException("")
        try:
            users = r.json()
        except JSONDecodeError:
            users = []
        return users

    @retry
    def join(self):
        r = requests.post('{}/join'.format(self.url), json={'name': self._user_name}, timeout=self._timeout)
        if r.status_code != 200:
            raise ChatException("")
