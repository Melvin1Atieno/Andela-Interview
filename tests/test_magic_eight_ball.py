
from magic_eight_ball import magic_eight_ball

import unittest

class TestMagicEightBall(unittest.TestCase):

    def test_magic_8_ball_requests_for_user_input(self):
        results = magic_eight_ball()
        self.assertIn("Enter your question",results)

    
if __name__ == "__main__":
    unittest.main()