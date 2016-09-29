
class User:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name

    def __str__(self):
        return 'User {}'.format(self.name)

    def __repr__(self):
        return '<User ip={s.ip} name={s.name}>'.format(s=self)
