from functools import partial

from blessed import Terminal

from .config import ConfigMixin

raw_print = partial(print, end='', flush=True)


class ChatSceen(ConfigMixin):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self._t = Terminal()
        self.messages = []

    def run(self):
        message = ''
        with self._t.fullscreen():
            with self._t.cbreak():
                self.redraw()
                while True:
                    val = self._t.inkey()
                    if val.name == 'KEY_ENTER':
                        self.messages.insert(0, message)
                        message = ''
                        self.redraw()
                    else:
                        message += str(val)
                        self.redraw_message_line(message)

    def redraw(self):
        self.redraw_messages()
        self.redraw_message_line('')

    def redraw_messages(self):
        for x, msg in enumerate(self.messages[:self._t.height-2], 2):
            raw_print(
                self._t.move(self._t.height-x, 0) + self._t.clear_eol + msg,
            )

    def redraw_message_line(self, message):
        raw_print(
            self._t.move(self._t.height, 0) + self._t.clear_eol + '{}: '.format(self.user_name) + message,
        )
