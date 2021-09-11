import main
import unittest
from fractions import Fraction

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)
    
    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(Exception):
            main.sum(2, 'Ala ma kota123')

    def test_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(3, 5), Fraction(1, 2)), Fraction(11, 10))
        self.assertEqual(main.sum(Fraction(3, 5), Fraction(2, 5)), Fraction(1, 1))

    def test_complex_complex(self):
        self.assertEqual(main.sum(complex(1, 2), complex(3, 4)), complex(4, 6))


if __name__ == '__main__':
    unittest.main()
