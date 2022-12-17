def hello():
    print('wellcome to my_phone_book')
    print('press 1 for add new contact')
    print('press 2 for find contact')
    command = input()
    return command

def get_tel():
    tel = input('tel = ')
    return tel

def get_name():
    name = input('name = ')
    return name