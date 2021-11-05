import unittest
from DeanerySystem import Day, Term, Lesson, Teacher, Timetable1 

class Test_TestTeacher(unittest.TestCase):

    def test_teacher_str(self):
        tea0 = Teacher('Jan', 'Testowy')
        self.assertEqual(str(tea0), 'Jan Testowy')

    def test_lesson_init_teacher(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.MON), "-", "-", 2)
        self.assertEqual(les0.teacher, None)

    def test_lesson_add_teacher(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        les0 + tea0
        self.assertEqual(les0.teacher, tea0)

    def test_lesson_sub_teacher(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        les0 + tea0
        les0 - tea0
        self.assertEqual(les0.teacher, None)

    def test_lesson_add_filled(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        tea1 = Teacher('Jan Paweł', 'Testowy')
        les0 + tea0
        les0 + tea1
        self.assertEqual(les0.teacher, tea1)

    def test_lesson_sub_empty(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        self.assertEqual(les0 - tea0, None)

    def test_lesson_add_hours(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        les0 + tea0
        self.assertEqual(les0.teacher.minute_count, 90)

    def test_lesson_sub_hours(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        les0 + tea0
        les0 - tea0
        self.assertEqual(tea0.minute_count, 0)

    def test_lesson_add_to_limit(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        les1 = Lesson(tt0, Term(17, 35, Day.WED), "-", "-", 2)
        les2 = Lesson(tt0, Term(17, 35, Day.MON), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        les0 + tea0
        les1 + tea0
        les2 + tea0
        self.assertEqual(tea0.minute_count, 270)

    def test_lesson_add_over_limit(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(17, 35, Day.SAT), "-", "-", 2)
        les1 = Lesson(tt0, Term(17, 35, Day.WED), "-", "-", 2)
        les2 = Lesson(tt0, Term(17, 35, Day.MON), "-", "-", 2)
        les3 = Lesson(tt0, Term(17, 35, Day.TUE), "-", "-", 2)
        tea0 = Teacher('Jan', 'Testowy')
        les0 + tea0
        les1 + tea0
        les2 + tea0
        les3 + tea0
        self.assertEqual(les3.teacher, None)

if __name__ == '__main__':
    unittest.main()
