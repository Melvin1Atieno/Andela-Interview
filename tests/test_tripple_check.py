import unittest

class TestTrippleCheck(unittest.TestCase):


    def test_tripple_check_returns_desired_output_output(self):
        resuts = tripple_check([5, 3, 4, 3, 5, 5, 3])
        self.assertEqual(4,results)


if __name__ == "__main__":
    unittest.main()