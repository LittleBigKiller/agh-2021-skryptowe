
import unittest
from DeanerySystem import Day, Term, Lesson, Action, Break, Timetable2 

class Test_Timetable2(unittest.TestCase):

    def test_put_true(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tt0.put(les0), True)

    def test_put_false(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        les0 = Lesson(tt0, Term(9, 30, Day.TUE), "-", "-", 2)
        self.assertEqual(tt0.put(les0), False)

    def test_get_lesson(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        ter0 = Term(9, 35, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.get(ter0), les0)

    def test_get_None(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        ter0 = Term(9, 30, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        self.assertEqual(tt0.get(les0), None)

    def test_busy_true(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.busy(les0.term), True)

    def test_busy_false(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(tt0.busy(les0.term), False)

    def test_cbtt_ft_true(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, True), True)

    def test_cbtt_ft_false(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        ter0 = Term(9, 30, Day.TUE)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, True), False)

    def test_cbtt_nft_true(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.SAT)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, False), True)

    def test_cbtt_nft_false(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        ter0 = Term(9, 30, Day.SAT)
        ter1 = Term(11, 00, Day.TUE)
        les0 = Lesson(tt0, ter0, "-", "-", 2)
        tt0.put(les0)
        self.assertEqual(tt0.can_be_transferred_to(ter1, False), False)

    def test_parase(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        strl = ['d-', 'd+', 't-', 't+']
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(tt0.parse(strl), actl)

    def test_peform_skipBreakFalse(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        tt1 = Timetable2(bl)
        ter1 = Term(8, 0, Day.WED)
        les1 = Lesson(tt1, ter1, 'less1', 'less1', 2)
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        tt0.put(les1)
        tt1.skipBreaks = False
        tt1.put(les1)
        tt1.perform(actl)
        self.assertEqual(tt1.lesson_list, tt0.lesson_list)

    def test_peform_skipBreakTrue(self):
        bl = [Break(Term(9, 30, Day.MON, 5)), Break(Term(11, 5, Day.MON, 10))]
        tt0 = Timetable2(bl)
        tt1 = Timetable2(bl)
        ter1 = Term(8, 0, Day.WED)
        les1 = Lesson(tt1, ter1, 'less1', 'less1', 2)
        actl = [Action.DAY_EARLIER, Action.DAY_LATER, Action.TIME_EARLIER, Action.TIME_LATER]
        tt0.put(les1)
        tt1.skipBreaks = True
        tt1.put(les1)
        tt1.perform(actl)
        self.assertEqual(tt1.lesson_list, tt0.lesson_list)



if __name__ == '__main__':
    unittest.main()
