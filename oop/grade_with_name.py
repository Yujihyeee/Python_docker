'''
학생이름을 입력받고
국어 Kor, 영어 eng, 수학 math, 를 입력받아서
학생이름, 평균점수, 학점을 출력하시오.
'''


class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def average(self):
        return sum(self.scores) / len(self.scores)

    @staticmethod
    def main():
        grade = Grade(input('Input Student Name: '))
        for i in ['Korean', 'English', 'Math']:
            grade.addScores(int(input(f"score is {i}: \n")))
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
