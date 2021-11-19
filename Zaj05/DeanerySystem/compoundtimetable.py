from DeanerySystem import Term, Break, Lesson, Timetable1, Timetable2


class CompoundTimetable():

    def __init__(self):
        self.tt1_list = []
        self.tt2_list = []

    def add_elem(self, timetable):
        if type(timetable) is Timetable1:
            self.tt1_list.append(timetable)
            return True
        elif type(timetable) is Timetable2:
            self.tt2_list.append(timetable)
            return True
        else:
            return False

    def rem_elem(self, timetable):
        if type(timetable) is Timetable1:
            self.tt1_list.remove(timetable)
            return True
        elif type(timetable) is Timetable2:
            self.tt2_list.remove(timetable)
            return True
        else:
            return False

    def sum_tables(self):
        timesum = 0

        for tt1 in self.tt1_list:
            for les in list(tt1.lesson_dict.values()):
                timesum += les.term.duration

        for tt2 in self.tt2_list:
            for les in list(tt2.lesson_dict.values()):
                timesum += les.term.duration
            for bre in tt2.breaks:
                timesum += bre.term.duration

        return timesum
