from configparser import ConfigParser

from dialog import Dialog

CONFIG_FILE = 'chat.ini'
DEFAULT_CONFIG = {
    'tracker': {'url': 'http://localhost:5000', 'timeout': 0.1},
    'user': {'name': ''},
}


def get_config():
    config = ConfigParser()
    config.read_dict(DEFAULT_CONFIG)
    config.read(CONFIG_FILE)
    return config


def save_config(config):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def update_name_from_user(config):
    default = config['user']['name']
    name = get_name_from_user(default)
    config['user']['name'] = name


def get_name_from_user(default=''):
    dialog = Dialog()
    while True:
        code, name = dialog.inputbox('Napis jmeno', init=default)
        if code == dialog.OK and name:
            break
    return name


class ConfigMixin:
    def __init__(self, config):
        self._config = config

    @property
    def tracker_url(self):
        return self._config['tracker']['url']

    @property
    def tracker_timeout(self):
        return float(self._config['tracker']['timeout'])

    @property
    def user_name(self):
        return self._config['user']['name']
