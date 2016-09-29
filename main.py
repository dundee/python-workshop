from configparser import ConfigParser

from blessed import Terminal
from dialog import Dialog
import json
import requests

CONFIG_FILE = 'chat.ini'
DEFAULT_CONFIG = {
    'tracker': {'url': 'http://localhost:5000', 'timeout': 0.1},
    'user': {'name': ''},
}


def main():
    config = get_config()
    name = get_name_with_config(config)
    save_config(config)

    join(config['tracker']['url'], float(config['tracker']['timeout']), name)
    print(get_users(config['tracker']['url'], float(config['tracker']['timeout'])))

    #do_chat(name)


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
    term = Terminal()

    messages = []
    message = ''

    with term.fullscreen():
        with term.cbreak():
            redraw_screen(term, name, messages)
            while True:
                val = term.inkey()
                if val.name == 'KEY_ENTER':
                    messages.insert(0, message)
                    message = ''
                    redraw_screen(term, name, messages)
                else:
                    message += str(val)
                    new_message_line(term, name, message)


def redraw_screen(term, name, messages):
    show_messages(term, messages)
    new_message_line(term, name, '')


def show_messages(term, messages):
    for x, msg in enumerate(messages[:term.height-2], 2):
        print(
            term.move(term.height-x, 0) + term.clear_eol + msg,
            end='',
            flush=True
        )


def new_message_line(term, name, message):
    print(
        term.move(term.height, 0) + term.clear_eol + '{}: '.format(name) + message,
        end='',
        flush=True
    )


def get_users(tracker_url, timeout):
    r = requests.get('{}/users'.format(tracker_url), timeout=timeout)
    return r.json()


def join(tracker_url, timeout, name):
    requests.post('{}/join'.format(tracker_url), json={'name': name}, timeout=timeout)


main()
