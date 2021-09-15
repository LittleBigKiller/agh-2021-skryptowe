import unittest
from DeanerySystem import Day, Term, Lesson, Timetable1 

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_earlierDay_ft_true(self):
        tt0 = Timetable1()
        lesson0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(lesson0.earlierDay(), True)

    def test_earlierDay_ft_false(self):
        tt0 = Timetable1()
        lesson1 = Lesson(tt0, Term(9, 35, Day.MON), "-", "-", 2)
        self.assertEqual(lesson1.earlierDay(), False)

    def test_earlierDay_nft_true(self):
        tt0 = Timetable1()
        lesson2 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        self.assertEqual(lesson2.earlierDay(), True)

    def test_earlierDay_nft_false(self):
        tt0 = Timetable1()
        lesson3 = Lesson(tt0, Term(9, 35, Day.SAT), "-", "-", 2)
        self.assertEqual(lesson3.earlierDay(), False)
    

    def test_laterDay_ft_true(self):
        tt0 = Timetable1()
        lesson0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(lesson0.laterDay(), True)

    def test_laterDay_ft_false(self):
        tt0 = Timetable1()
        lesson1 = Lesson(tt0, Term(17, 35, Day.THU), "-", "-", 2)
        self.assertEqual(lesson1.laterDay(), False)

    def test_laterDay_nft_true(self):
        tt0 = Timetable1()
        lesson2 = Lesson(tt0, Term(14, 35, Day.SAT), "-", "-", 2)
        self.assertEqual(lesson2.laterDay(), True)

    def test_laterDay_nft_false(self):
        tt0 = Timetable1()
        lesson3 = Lesson(tt0, Term(9, 35, Day.SUN), "-", "-", 2)
        self.assertEqual(lesson3.laterDay(), False)


    def test_earlierTime_ft_true(self):
        tt0 = Timetable1()
        lesson0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(lesson0.earlierTime(), True)

    def test_earlierTime_ft_false(self):
        tt0 = Timetable1()
        lesson1 = Lesson(tt0, Term(8, 5, Day.MON), "-", "-", 2)
        self.assertEqual(lesson1.earlierTime(), False)

    def test_earlierTime_nft_true(self):
        tt0 = Timetable1()
        lesson2 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        self.assertEqual(lesson2.earlierTime(), True)

    def test_earlierTime_nft_false(self):
        tt0 = Timetable1()
        lesson3 = Lesson(tt0, Term(17, 35, Day.FRI), "-", "-", 2)
        self.assertEqual(lesson3.earlierTime(), False)
    

    def test_laterTime_ft_true(self):
        tt0 = Timetable1()
        lesson0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(lesson0.laterTime(), True)

    def test_laterTime_ft_false(self):
        tt0 = Timetable1()
        lesson1 = Lesson(tt0, Term(17, 35, Day.THU), "-", "-", 2)
        self.assertEqual(lesson1.laterTime(), False)

    def test_laterTime_nft_true(self):
        tt0 = Timetable1()
        lesson2 = Lesson(tt0, Term(14, 35, Day.SAT), "-", "-", 2)
        self.assertEqual(lesson2.laterTime(), True)

    def test_laterTime_nft_false(self):
        tt0 = Timetable1()
        lesson3 = Lesson(tt0, Term(17, 35, Day.SUN), "-", "-", 2)
        self.assertEqual(lesson3.laterTime(), False)



if __name__ == '__main__':
    unittest.main()
