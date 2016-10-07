from configparser import ConfigParser
import logging
import logging.config
from typing import Any, Mapping

from dialog import Dialog

CONFIG_FILE = 'chat.ini'
DEFAULT_CONFIG = {
    'tracker': {'url': 'http://localhost:5000', 'timeout': 0.1},
    'user': {'name': ''},
    'server': {'port': 9000},
    'database': {'file': 'chat.db'},
}  # type: Mapping[str, Mapping[str, Any]]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'chat.log',
            'mode': 'a+',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['logfile'],
        },
        'requests': {
            'level': 'INFO',
        },
        'werkzeug': {
            'level': 'WARNING',
        },
    },
}


# logging.basicConfig(
#     filename='chat.log',
#     format='[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
#     level=logging.DEBUG,
# )

logging.config.dictConfig(LOGGING)


def get_config() -> ConfigParser:
    config = ConfigParser()
    config.read_dict(DEFAULT_CONFIG)
    config.read(CONFIG_FILE)
    return config


def save_config(config: ConfigParser):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def update_name_from_user(config: ConfigParser):
    default = config['user']['name']
    name = get_name_from_user(default)
    config['user']['name'] = name


def get_name_from_user(default: str='') -> str:
    dialog = Dialog()
    while True:
        code, name = dialog.inputbox('Napis jmeno', init=default)
        if code == dialog.OK and name:
            break
    return name


class ConfigMixin:
    def __init__(self, config: ConfigParser) -> None:
        self._config = config

    @property
    def tracker_url(self) -> str:
        return self._config['tracker']['url']

    @property
    def tracker_timeout(self) -> float:
        return float(self._config['tracker']['timeout'])

    @property
    def user_name(self) -> str:
        return self._config['user']['name']

    @property
    def server_port(self) -> str:
        return self._config['server']['port']
