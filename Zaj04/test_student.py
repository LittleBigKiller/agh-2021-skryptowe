import unittest
from DeanerySystem import Day, Term, Lesson, Student, Timetable1
from slist import slist

class Test_StudentLesson(unittest.TestCase):

    def test_student_idgen(self):
        stu0 = slist[0]
        stu1 = slist[1]
        stu2 = slist[2]
        self.assertEqual(stu0.getId(), 0)
        self.assertEqual(stu1.getId(), 1)
        self.assertEqual(stu2.getId(), 2)

    def test_student_str(self):
        stu0 = Student('Jan', 'Testowy')
        self.assertEqual(str(stu0), 'Jan Testowy')

    def test_lesson_get_sid_list(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        self.assertEqual(les0.student_id, [])

    def test_lesson_add_valid_sid(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        les0 + 0
        self.assertEqual(les0.student_id, [0])

    def test_lesson_add_invalid_sid(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        les0 + 330
        self.assertEqual(les0.student_id, [])

    def test_lesson_add_sid_when_max(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        les0 + 0; les0 + 1; les0 + 2; les0 + 3; les0 + 4
        les0 + 5; les0 + 6; les0 + 7; les0 + 8; les0 + 9
        les0 + 10; les0 + 11; les0 + 12
        self.assertEqual(les0.student_id, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_lesson_sub_valid_sid(self):
        tt0 = Timetable1()
        les0 = Lesson(tt0, Term(9, 35, Day.TUE), "-", "-", 2)
        les0 + 0
        les0 - 0
        self.assertEqual(les0.student_id, [])


if __name__ == '__main__':
    unittest.main()
