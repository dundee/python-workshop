from functools import partial

from blessed import Terminal

from .config import ConfigMixin


raw_print = partial(print, end='', flush=True)


class ChatSceen(ConfigMixin):
    def __init__(self, tracker, sender, messages, *args, **kwds):
        super().__init__(*args, **kwds)
        self._t = Terminal()
        self.tracker = tracker
        self.sender = sender
        self.messages = messages
        self.message = ''

    def run(self):
        with self._t.fullscreen():
            with self._t.cbreak():
                self.redraw()
                while True:
                    val = self._t.inkey(timeout=1)
                    if val.name == 'KEY_ENTER':
                        self.send_message()
                    else:
                        self.message += str(val)
                    self.redraw()

    def redraw(self):
        self.redraw_messages()
        self.redraw_message_line()

    def redraw_messages(self):
        for x, msg in enumerate(list(self.messages)[:self._t.height-2], 2):
            raw_print(
                self._t.move(self._t.height-x, 0) + self._t.clear_eol + msg,
            )

    def redraw_message_line(self):
        raw_print(
            self._t.move(self._t.height, 0) + self._t.clear_eol + '{}: '.format(self.user_name) + self.message,
        )

    def show_error(self, error_message):
        raw_print(self._t.move(0, 0) + self._t.clear_eol + error_message)

    def send_message(self):
        self.messages.add(self.message)
        users = self.tracker.get_users()
        for user in users:
            try:
                self.sender.send_message_to_user(user, self.message)
            except Exception as exc:
                self.show_error('Problem sending message to user {}: {}'.format(user.name, str(exc)))
        self.message = ''
