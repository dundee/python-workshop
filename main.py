from dialog import Dialog


def get_name():
    dialog = Dialog()

    while True:
        code, name = dialog.inputbox('Napis jmeno')
        if code == dialog.OK and name:
            break
    return name


print(get_name())
