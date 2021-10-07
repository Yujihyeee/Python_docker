'''
파이썬에서 루프 형태는 3가지가 있다.
'''
from icecream import ic


class OneToTenSum(object):

    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(1, 11):
            sum += i
        return sum

    def one_to_ten_sum_2(self):
        val = sum(i for i in range(1, 11))
        return val

    def one_to_ten_sum_3(self):
        val = sum(range(1, 11))
        return val



