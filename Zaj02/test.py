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

    def test_just_word_match(self):
        self.assertEqual(skrypt.match_word("Ala")[1], "Ala")

    def test_just_word_start(self):
        self.assertEqual(skrypt.match_word("Ala")[0], 0)

    def test_just_number_match(self):
        self.assertEqual(skrypt.match_number("1231")[1], "1231")

    def test_just_number_start(self):
        self.assertEqual(skrypt.match_number("1231")[0], 0)

    def test_leading_space_word_match(self):
        self.assertEqual(skrypt.match_word("    1231Ala")[1], "Ala")

    def test_leading_space_word_start(self):
        self.assertEqual(skrypt.match_word("    1231Ala")[0], 8)

    def test_leading_space_number_match(self):
        self.assertEqual(skrypt.match_number("    1231Ala")[1], "1231")

    def test_leading_space_number_start(self):
        self.assertEqual(skrypt.match_number("    1231Ala")[0], 4)


if __name__ == '__main__':
    unittest.main()

