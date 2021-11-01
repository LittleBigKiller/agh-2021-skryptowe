import unittest
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.term import Term


class Test_TestDeanerySystem(unittest.TestCase):

    def test_sameDate(self):
        term = Term(Day.MON, 8, 0)
        term.setTerm('27 X 2021 8:00 - 27 X 2021 9:30')
        self.assertEqual(str(term), 'Środa 8:00 [90]')

    def test_diffDay(self):
        term = Term(Day.MON, 8, 0)
        term.setTerm('27 X 2021 8:00 - 28 X 2021 8:00')
        self.assertEqual(str(term), 'Środa 8:00 [1440]')



if __name__ == '__main__':
    unittest.main()
