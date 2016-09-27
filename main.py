
def get_name():
    while True:
        print('Napis jmeno:', end='')
        name = input()
        if name:
            break
    return name


print(get_name())
