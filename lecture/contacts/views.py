from lecture.contacts.models import Contacts
from lecture.menu.models import print_menu

if __name__ == '__main__':
    ls = []
    while 1:
        menu = print_menu(['exit', 'add', 'print', 'delete'])
        if menu == '0':
            break
        elif menu == 1:
            t = Contacts.set_contact()
            ls.append(t)
        elif menu == 2:
            Contacts.get_contacts(ls)
        elif menu == 3:
            Contacts.del_contact(ls, input('Del Name'))
            break
