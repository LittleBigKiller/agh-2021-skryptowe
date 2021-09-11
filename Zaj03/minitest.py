import unittest
from DeanerySystem.day import Day
from DeanerySystem.term import Term


class Test_TestIncrementDecrement(unittest.TestCase):

    def test_earlierThan(self):
        self.assertTrue(Term(Day.TUE, 9, 45).earlierThan(Term(Day.WED, 10, 15)))
        self.assertTrue(Term(Day.TUE, 9, 45).earlierThan(Term(Day.TUE, 10, 15)))
        self.assertTrue(Term(Day.TUE, 9, 45).earlierThan(Term(Day.TUE, 9, 50)))
        self.assertFalse(Term(Day.TUE, 9, 45).earlierThan(Term(Day.TUE, 9, 40)))

    def test_laterThan(self):
        self.assertTrue(Term(Day.WED, 10, 15).laterThan(Term(Day.TUE, 9, 45)))
        self.assertTrue(Term(Day.TUE, 10, 15).laterThan(Term(Day.TUE, 9, 45)))
        self.assertTrue(Term(Day.TUE, 9, 50).laterThan(Term(Day.TUE, 9, 45)))
        self.assertFalse(Term(Day.TUE, 9, 40).laterThan(Term(Day.TUE, 9, 45)))

    def test_equals(self):
        self.assertTrue(Term(Day.TUE, 9, 45).equals(Term(Day.TUE, 9, 45)))
        self.assertFalse(Term(Day.TUE, 9, 40).equals(Term(Day.TUE, 9, 45)))


if __name__ == '__main__':
    unittest.main()