from typing import List

from DeanerySystem.day import Day
from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.action import Action
from DeanerySystem.basictimetable import BasicTimetable


class Timetable1(BasicTimetable):

    def __init__(self):
        super().__init__()

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        if term.hour < 8:
            return False

        et = term.getEndTime()
        if et[0] > 20:
            return False
        if et[0] == 20 and et[1] > 0:
            return False

        if not self.busy(term):
            if term.day.value < 5:
                is_ft = True
            elif term.day.value > 5:
                is_ft = False
            else:
                if term.hour < 17:
                    is_ft = True
                else:
                    is_ft = False

            if is_ft == full_time:
                return True
        return False

    def busy(self, term: Term) -> bool:
        for les in list(self.lesson_dict.values()):
            if les.term == term:
                return True

            les_start = (les.term.hour, les.term.minute)
            les_end = les.term.getEndTime()
            ter_start = (term.hour, term.minute)
            ter_end = term.getEndTime()

            if les_end > ter_start and les_end < ter_end:
                return True
            if ter_end > les_start and ter_end < les_end:
                return True
            if les_start > ter_start and les_start < ter_end:
                return True
            if ter_start > les_start and ter_start < les_end:
                return True

        return False

    def __str__(self):
        timetab = []
        for les in list(self.lesson_dict.values()):
            timetab.append(les.term)
        timetab = sorted(timetab, key=lambda t: t.printStartTime())

        disptab = []
        for i in range(8):
            disptab.append([])
            for j in range(len(timetab) + 1):
                disptab[i].append('')

        for d in Day:
            disptab[d.value][0] = str(d)

        for c, t in enumerate(timetab):
            disptab[0][c + 1] = f'{t.printStartTime()}-{t.printEndTime()}'

        for les in list(self.lesson_dict.values()):
            disptab[les.term.day.value][timetab.index(les.term) + 1] = les.name

        b = ''
        bl = f'\n{b: ^12}{b:*^92}\n'
        em = f'{b: ^12}'

        finstr = ''
        for tc in range(len(timetab) + 1):
            for dc in range(8):
                finstr += f'{disptab[dc][tc]: ^12}*'
            finstr += bl

        return finstr
