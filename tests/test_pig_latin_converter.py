from pig_latin_converter import pig_latin_converter

import unittest

class TestPigLatinConverter(unittest.TestCase):

    def test_pig_latin_converter_for_non_alternating_numbers_adding_up_to_10(self):
        results = pig_latin_converter("arrb6???4xxbl5???eee5")
        self.assertEqual(True,results)

    def test_pig_latin_converter_with_non_alternating_numbers_not_adding_up_to_10(self):
        results = pig_latin_converter("acc?7??sss?3rr1??????5")
        self.assertEqual(True,results)

    def test_pig_latin_converter_with_more_than_3_question_marks_between_numbers_adding_up_to_10(self):
        results = pig_latin_converter("acc?7??sss?3rr1??????5")
        self.assertEqual(True,results)

    def test_pig_latin_converter_with_numbers_adding_up_to_10_with_less_than_three_question_marks(self):
        results = pig_latin_converter("5??aaaaaaaaaaaaaaaaaaa?5?5")
        self.assertEqual(False,results)

    def test_pig_latin_converter_with_alternating_numbers_adding_up_to_10_and_three_question_marks(self):
        results = pig_latin_converter("9???1???9???1???9" )
        self.assertEqual(True,results)

    def test_pig_latin_converter_with_a_question_mark_and_numbers_not_adding_up_to_10(self):
        results = pig_latin_converter("aa6?9")
        self.assertEqual(False,results)



    

    


if __name__ == "__main__":
    unittest.main()