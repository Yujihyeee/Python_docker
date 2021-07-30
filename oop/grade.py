'''
국어 Kor, 영어 eng, 수학 math, 를 입력받아서
평균값으로 학점 A ~ F를 출력하시오.
'''


class Grade(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def average(self):
        return self.sum() / 3

    @staticmethod
    def main():
        kor = int(input("Korean: \n"))
        eng = int(input("English: \n"))
        math = int(input("Math: \n"))
        grade = Grade(kor, eng, math)
        average = grade.average()

        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        elif average >= 0:
            grade = 'F'
        print(f"Grade is {grade}.")


Grade.main()
