from json.decoder import JSONDecodeError

import requests

from .config import ConfigMixin
from .exceptions import ChatException
from .model import User
from .retry import retry


class TrackerClient(ConfigMixin):
    @retry(3)
    def get_users(self):
        r = requests.get('{}/users'.format(self.tracker_url), timeout=self.tracker_timeout)
        if r.status_code != 200:
            raise ChatException('')
        try:
            users = r.json()
        except JSONDecodeError:
            users = []
        return [User(user['ip'], user['name']) for user in users]

    @retry(5)
    def join(self):
        r = requests.post('{}/join'.format(self.tracker_url), json={'name': self.user_name}, timeout=self.tracker_timeout)
        if r.status_code != 200:
            raise ChatException('')
