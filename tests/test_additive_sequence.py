from additive_sequence import additive_sequence

import unittest

class TestAdditiveSequence(unittest.TestCase):

    def test_additive_sequence_returns_true_for_additive_sequence(self):
        results = additive_sequence([6, 6, 12, 18, 30])
        self.assertEqual(True,results)

    def test_additive_sequence_returns_false_for_additive_sequence(self):
        results = additive_sequence([6, 6, 1, 18, 30])
        self.assertEqual(False,results)

    def test_additive_sequence_only_accepts_a_list_of_integers(self):
        results = additive_sequence([1,2,'a','b','c'])
        self.assertEqual(False,results)
    
    def test_additive_sequence_returns_false_for_ist_of_two(self):
        results = additive_sequence([1,2])
        self.assertEqual(False,results)


if __name__ == "__main__":
    unittest.main()
