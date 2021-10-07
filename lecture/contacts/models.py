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

    @staticmethod
    def set_contact() -> object:
        return Contacts(input('name'), int(input('phone')), input('email'), input('address'))

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.to_string()

    @staticmethod
    def del_contact(ls, name):
        for i, v in enumerate(ls):
            if name == v.name:
                del ls[i]
