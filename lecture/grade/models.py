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


'''
학생이름을 입력받고
국어 Kor, 영어 eng, 수학 math, 를 입력받아서
학생이름, 평균점수, 학점을 출력하시오.
'''


class Grade(object):
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores)

    @staticmethod
    def main():
        grade = Grade(input('Input Student Name: '))
        for i in ['Korean', 'English', 'Math']:
            grade.add_scores(int(input(f"score is {i}: \n")))
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
