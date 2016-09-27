from configparser import ConfigParser

from dialog import Dialog

CONFIG_FILE = 'chat.ini'
DEFAULT_CONFIG = {'user': {'name': ''}}


def main():
    config = get_config()
    name = get_name_with_config(config)
    save_config(config)

    do_chat(name)


def get_config():
    config = ConfigParser()
    config.read_dict(DEFAULT_CONFIG)
    config.read(CONFIG_FILE)
    return config


def save_config(config):
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def get_name_with_config(config):
    default = config['user']['name']
    name = get_name(default)
    config['user']['name'] = name
    return name


def get_name(default=''):
    dialog = Dialog()
    while True:
        code, name = dialog.inputbox('Napis jmeno', init=default)
        if code == dialog.OK and name:
            break
    return name


def do_chat(name):
    while True:
        print("{}:".format(name), end='')
        msg = input()


main()
