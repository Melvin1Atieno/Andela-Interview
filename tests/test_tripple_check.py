from tripple_check import tripple_check
import unittest

class TestTrippleCheck(unittest.TestCase):


    def test_tripple_check_returns_desired_output(self):
        results = tripple_check([5, 3, 4, 3, 5, 5, 3])
        self.assertEqual(4,results)

    def test_tripple_check_returns_msg_for_list_with_all_tripples(self):
        results = tripple_check([5,3,3,3,4,5,4,5,4])
        self.assertEqual('List Contains all tripples',results)

    def test_tripple_check_return_comma_seperated_integers_for_values_not_in_trippl(self):
        results = tripple_check([5, 3, 4, 3, 5, 5, 3,7])
        self.assertEqual((4,7),results)

if __name__ == "__main__":
    unittest.main()