import unittest

from basic.one_to_ten_sum import One_to_ten_sum


class OneToTenSumTest(unittest.TestCase):
    mock = One_to_ten_sum()

    def test_One_to_ten_sum1(self):
        self.mock.one_to_ten_sum_1()

    def test_one_to_ten_sum_2(self):
        self.mock.one_to_ten_sum_2()

if __name__ == '__main__':
    unittest.main()
