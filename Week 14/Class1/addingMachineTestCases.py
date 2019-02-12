import unittest

from addingMachine import add
# could import * if there are several functions you want to test.

class Tests(unittest.TestCase):

    def test_add_intergers(self):

        num1 = 2
        num2 = 3
        expectedResult = 5
    # this is Arrange

        result = add(num1, num2)
    # this is Act

        self.assertEqual(expectedResult, result)
    # this is Assert

    def test_add_floats(self):
        num1 = 2.0
        num2 = 3.0
        expectedResult = 5.0
        # this is Arrange

        result = add(num1, num2)
        # this is Act

        self.assertEqual(expectedResult, result)
    # this is Assert

