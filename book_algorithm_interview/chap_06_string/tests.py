import unittest
from book_algorithm_interview.chap_06_string.models import Palindrome2


class TestPalindrome(unittest.TestCase):
    def test_str_to_list(self):
        instance = Palindrome2()
        instance.input_string = '수박이박수호호'
        res1 = instance.isPalindrome()
        self.assertEqual(res1, {'RESULT': False})

    def test_reverse_string(self):
        instance = Palindrome2()
        instance.input_string = '수박이박수호호'
        res = instance.reverse_string()
        self.assertEqual(res, ['호', '호', '수', '박', '이', '박', '수'])


if __name__ == '__main__':
    unittest.main()