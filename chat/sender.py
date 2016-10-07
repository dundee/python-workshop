import requests

from .config import ConfigMixin
from .exceptions import ChatException
from .model import User
from .retry import retry


class Sender(ConfigMixin):
    @retry(3)
    def send_message_to_user(self, user: User, message: str) -> None:
        r = requests.post('http://{}:{}/'.format(user.ip, self.server_port), json={
            'message': message,
            'user_name': self.user_name,
        })
        if r.status_code != 200:
            raise ChatException(r)
