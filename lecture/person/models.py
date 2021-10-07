'''
이름, 나이, 주소를 입력받아서 자기소개하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다.로 됩니다.
이때 여러 사람이면 전부 입력받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''


class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        print(f'my name is {self.name}, age is {self.age}, address is {self.address}.')
