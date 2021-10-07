from lecture.person.models import Person

if __name__ == '__main__':
    persons = []
    while 1:
        print('0. Exit 1. Add 2. Print')
        menu = input('Choose number: ')
        if menu == '0':
            break
        elif menu == '1':
            persons.append(Person(input('name'), input('age'), input('address')))
        elif menu == '2':
            for i in persons:
                i.introduce()
