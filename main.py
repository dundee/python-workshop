from threading import Thread

from blessed import Terminal

from chat.chat_screen import ChatSceen
from chat.config import get_config, update_name_from_user, save_config
from chat.model import Messages
from chat.sender import Sender
from chat.server import run_server
from chat.tracker_client import TrackerClient


def main():
    config = get_config()
    update_name_from_user(config)
    save_config(config)

    tracker = TrackerClient(config=config)
    tracker.join()

    messages = Messages(config['database'])
    messages.load()

    thread = Thread(target=run_server, daemon=True, kwargs={'config': config, 'messages': messages})
    thread.start()

    sender = Sender(config)

    try:
        ChatSceen(config=config, tracker=tracker, sender=sender, messages=messages).run()
    except KeyboardInterrupt:
        messages.save()
        print(Terminal().clear())


if __name__ == '__main__':
    main()
