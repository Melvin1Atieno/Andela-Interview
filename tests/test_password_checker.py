from password_checker import check_password

import unittest

class TestPasswordChecker(unittest.TestCase):

    def test_password_checker_checks_for_atleast_one_letter_between_a_z(self):
        results = check_password("12345A#")
        self.assertEqual("password must have atleast 1 letter between a-z", results)

    def test_password_checker_checks_for_atleast_one_number_between_0_9(self):
        results = check_password("abcdC#$")
        self.assertEqual("password must have atleast one number between 0-9",results)

    def test_password_checker_checks_for_letters_between_A_Z(self):
        results = check_password("abcd#$12")
        self.assertEqual("password must have atleast one letter between A-Z",results)
    
    def test_checker_checks_for_a_character(self):
        results = check_password("123abcAAD")
        self.assertEqual("password must have atleast one character from #$@",results)

    def test_password_checker_checks_for_minimum_length_of_6_characters(self):
        results = check_password("1aAB#")
        self.assertEqual("minimum length should be 6 characters",results)

    def test_password_checker_checks_for_maximum_length_of_12(self):
        results = check_password("aA1@asdgxcfer")
        self.assertEqual("maximum password length 12",results)

    def test_password_checker_returns_comma_separated_valid_passwords(self):
        results = check_password("2w3E,ABd1234@1,aF1#,2We3345")
        self.assertEqual("ABd1234@1",results)

    
if __name__ == "__main__":
    unittest.main()