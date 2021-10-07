'''
name, phone, email, address
'''


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


    def to_string(self):
        print(f'name is {self.name}, phone is {self.phone}, email is {self.email}, address is {self.address}.')


def set_contact() -> object:
    return Contacts(input('name'), int(input('phone')), input('email'), input('address'))


def get_contacts(ls):
    for i in ls:
        i.to_string()


def del_contact(ls, name):
    for i, v in enumerate(ls):
        if name == v.name:
            del ls[i]


def print_menu(ls) -> int:
    # return '\t'.join(ls)
    t = ''
    for i, v in enumerate(ls):
        t += str(i) + '-' + v + '\t'
    return int(input(t))


def main():
    ls = []
    while 1:
        menu = print_menu(['exit', 'add', 'print', 'delete'])
        if menu == '0':
            return
        elif menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contacts(ls)
        elif menu == 3:
            del_contact(ls, input('Del Name'))
            break
