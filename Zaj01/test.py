import main
import unittest
from fractions import Fraction

class Test_SumFunction(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)
    
    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_text(self):
        with self.assertRaises(ValueError):
            main.sum(2, 'Ala ma kota123')

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(3, 5), Fraction(1, 2)), Fraction(11, 10))
        self.assertEqual(main.sum(Fraction(3, 5), Fraction(2, 5)), Fraction(1, 1))

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(1, 2), complex(3, 4)), complex(4, 6))

    def test_sum_complex_fraction(self):
        self.assertEqual(main.sum(complex(0.2, 4), Fraction(9, 5)), complex(2, 4))

    def test_sum_fraction_complex(self):
        self.assertEqual(main.sum(Fraction(9, 5), complex(0.2, 4)), complex(2, 4))

    def test_sum_integer_bad_type(self):
        with self.assertRaises(TypeError):
            main.sum(1, [2, 3])


if __name__ == '__main__':
    unittest.main()
