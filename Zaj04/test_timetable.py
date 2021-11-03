
import unittest
from DeanerySystem import Day, Term, Lesson, Action, Timetable1 

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_put_true(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tt0.put(les0), True)

    def test_put_false(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.put(les0), False)

    def test_get_lesson(self):
        tt0 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.get(ter0), les0)

    def test_get_None(self):
        tt0 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        self.assertEqual(tt0.get(les0), None)

    def test_busy_match(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.busy(les0.term), True)

    def test_busy_overlap(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        ter0 = Term(9, 00, Day.TUE)
        tt0.put(les0)
        self.assertEqual(tt0.busy(ter0), True)

    def test_busy_false(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tt0.busy(les0.term), False)

    def test_cbtt_ft_true(self):
        tt0 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, True), True)

    def test_cbtt_ft_false(self):
        tt0 = Timetable1()
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, True), False)

    def test_cbtt_nft_true(self):
        tt0 = Timetable1()
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, False), True)

    def test_cbtt_nft_false(self):
        tt0 = Timetable1()
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, False), False)

    def test_parase(self):
        tt0 = Timetable1()
        strl = ['d-', 'd+', 't-', 't+']
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(tt0.parse(strl), actl)

    def test_peform(self):
        tt0 = Timetable1()
        tt1 = Timetable1()
        ter1 = Term(8, 0, Day.WED)
        les1 = Lesson(tt1, ter1, 'less1', 'less1', 2)
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        tt0.put(les1)
        tt1.put(les1)
        tt1.perform(actl)
        self.assertEqual(tt1.lesson_list, tt0.lesson_list)


if __name__ == '__main__':
    unittest.main()
