from chat.chat_screen import ChatSceen
from chat.config import get_config, update_name_from_user, save_config
from chat.sender import Sender
from chat.tracker_client import TrackerClient


def main():
    config = get_config()
    update_name_from_user(config)
    save_config(config)

    tracker = TrackerClient(config)
    tracker.join()

    sender = Sender(config)

    try:
        ChatSceen(config=config, tracker=tracker, sender=sender).run()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
