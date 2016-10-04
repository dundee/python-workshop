from chat.chat_screen import ChatSceen
from chat.config import get_config, update_name_from_user, save_config
from chat.tracker_client import TrackerClient


def main():
    config = get_config()
    update_name_from_user(config)
    save_config(config)

    t = TrackerClient(config)
    t.join()
    print(t.get_users())

    try:
        ChatSceen(config).run()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
