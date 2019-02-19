import unittest


from .password_functions import *

class Test_PW_Functions(unittest.TestCase):

    def test_pw_not_long_enough_min(self):

        sample_pass = "abcd"
        expected_result = False

        result = validate_password_complexity(sample_pass)

        self.assertEqual(expected_result, result)

    def test_pw_just_long_enough_min(self):
        sample_pass = "abcdefgh"
        expected_result = True

        result = validate_password_complexity(sample_pass)

        self.assertEqual(expected_result, result)

    def test_pw_long_enough_min(self):
        sample_pass = "abcd"
        expected_result = True

        result = validate_password_complexity(sample_pass)

        self.assertEqual(expected_result, result)



