import skrypt
import unittest
import re

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_word_match(self):
        self.assertEqual(skrypt.match_word("1231Ala")[1], "Ala")

    def test_word_start(self):
        self.assertEqual(skrypt.match_word("1231Ala")[0], 4)

    def test_number_match(self):
        self.assertEqual(skrypt.match_number("1231Ala")[1], "1231")

    def test_number_start(self):
        self.assertEqual(skrypt.match_number("1231Ala")[0], 0)


if __name__ == '__main__':
    unittest.main()

