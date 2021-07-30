import unittest

from basic.palindrome import Palindrome


class PalindromeTest(unittest.TestCase):
    mock = Palindrome()


    def test_palindrome(self):
        self.mock.str_to_list()


if __name__ == '__main__':
    unittest.main()
