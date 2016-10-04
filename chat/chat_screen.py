from blessed import Terminal


class ChatSceen:
    def __init__(self, config):
        self._config = config
        self._t = Terminal()
        self.messages = []

    @property
    def _user_name(self):
        return self._config['user']['name']

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
            print(
                self._t.move(self._t.height-x, 0) + self._t.clear_eol + msg,
                end='',
                flush=True
            )

    def redraw_message_line(self, message):
        print(
            self._t.move(self._t.height, 0) + self._t.clear_eol + '{}: '.format(self._user_name) + message,
            end='',
            flush=True
        )
