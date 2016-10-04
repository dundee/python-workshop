import requests

from .config import ConfigMixin
from .retry import retry


class Sender(ConfigMixin):
    @retry(3)
    def send_message_to_user(self, user, message):
        requests.post(
            'http://{}:9000/send_message'.format(user.ip),
            json={'message': message, 'user_name': self.user_name}
        )
