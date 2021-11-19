import unittest
from DeanerySystem import Day, Term, Lesson, Action, Break, BasicTerm, Timetable1, Timetable2, CompoundTimetable


class Test_CompoundTimetable(unittest.TestCase):

    def test_add_tt1(self):
        cptt = CompoundTimetable()
        tt1 = Timetable1()
        self.assertTrue(cptt.add_elem(tt1))

    def test_add_tt2(self):
        cptt = CompoundTimetable()
        tt2 = Timetable2([])
        self.assertTrue(cptt.add_elem(tt2))

    def test_add_none(self):
        cptt = CompoundTimetable()
        self.assertFalse(cptt.add_elem(None))


    def test_rem_tt1(self):
        cptt = CompoundTimetable()
        tt1 = Timetable1()
        cptt.add_elem(tt1)
        self.assertTrue(cptt.rem_elem(tt1))

    def test_rem_tt2(self):
        cptt = CompoundTimetable()
        tt2 = Timetable2([])
        cptt.add_elem(tt2)
        self.assertTrue(cptt.rem_elem(tt2))

    def test_rem_none(self):
        cptt = CompoundTimetable()
        self.assertFalse(cptt.rem_elem(None))


    def test_sum_tt1(self):
        cptt = CompoundTimetable()
        tt1 = Timetable1()
        tt2 = Timetable1()
        les0 = Lesson(tt1, Term(8, 00, Day.MON), "-", "-", 2)
        les1 = Lesson(tt1, Term(9, 30, Day.MON), "-", "-", 2)
        les2 = Lesson(tt1, Term(11, 00, Day.MON), "-", "-", 2)
        les3 = Lesson(tt2, Term(8, 00, Day.WED), "-", "-", 2)
        les4 = Lesson(tt2, Term(9, 30, Day.WED), "-", "-", 2)
        les5 = Lesson(tt2, Term(11, 00, Day.WED), "-", "-", 2)
        tt1.put(les0)
        tt1.put(les1)
        tt1.put(les2)
        tt2.put(les3)
        tt2.put(les4)
        tt2.put(les5)

        cptt.add_elem(tt1)
        cptt.add_elem(tt2)

        self.assertEqual(cptt.sum_tables(), 540)
        
    def test_sum_tt2(self):
        cptt = CompoundTimetable()
        bl1 = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tt1 = Timetable2(bl1)
        tt2 = Timetable2(bl1)
        les0 = Lesson(tt1, Term(8, 00, Day.MON), "-", "-", 2)
        les1 = Lesson(tt1, Term(9, 35, Day.MON), "-", "-", 2)
        les2 = Lesson(tt1, Term(11, 15, Day.MON), "-", "-", 2)
        les3 = Lesson(tt2, Term(8, 00, Day.WED), "-", "-", 2)
        les4 = Lesson(tt2, Term(9, 35, Day.WED), "-", "-", 2)
        les5 = Lesson(tt2, Term(11, 15, Day.WED), "-", "-", 2)
        tt1.put(les0)
        tt1.put(les1)
        tt1.put(les2)
        tt2.put(les3)
        tt2.put(les4)
        tt2.put(les5)

        cptt.add_elem(tt1)
        cptt.add_elem(tt2)

        self.assertEqual(cptt.sum_tables(), 570)
        
    def test_sum_mix(self):
        cptt = CompoundTimetable()
        bl1 = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
        tt1 = Timetable1()
        tt2 = Timetable2(bl1)
        les0 = Lesson(tt1, Term(8, 00, Day.MON), "-", "-", 2)
        les1 = Lesson(tt1, Term(9, 35, Day.MON), "-", "-", 2)
        les2 = Lesson(tt1, Term(11, 15, Day.MON), "-", "-", 2)
        les3 = Lesson(tt2, Term(8, 00, Day.WED), "-", "-", 2)
        les4 = Lesson(tt2, Term(9, 35, Day.WED), "-", "-", 2)
        les5 = Lesson(tt2, Term(11, 15, Day.WED), "-", "-", 2)
        tt1.put(les0)
        tt1.put(les1)
        tt1.put(les2)
        tt2.put(les3)
        tt2.put(les4)
        tt2.put(les5)

        cptt.add_elem(tt1)
        cptt.add_elem(tt2)

        self.assertEqual(cptt.sum_tables(), 555)


if __name__ == '__main__':
    unittest.main()
