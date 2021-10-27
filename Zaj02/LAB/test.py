import skrypt
import unittest
import re

class Test_FoldComments(unittest.TestCase):
    def test_match_comment_open(self):
        self.assertEqual(skrypt.match_cc('/*'), True)

if __name__ == '__main__':
    unittest.main()

