from typing import List

from DeanerySystem.day import Day
from DeanerySystem.term import Term
from DeanerySystem.lesson import Lesson
from DeanerySystem.action import Action
from DeanerySystem.tbreak import Break
from DeanerySystem.basictimetable import BasicTimetable

class Timetable2(BasicTimetable):
    skipBreaks = False

    def __init__(self, breaks: List[Break]):
        self.breaks = breaks
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

    def overlapsBreak(self, term: Term) -> bool:
        ts = term.getStartTime()
        te = term.getEndTime()
        for bre in self.breaks:
            bs = bre.term.getStartTime()
            be = bre.term.getEndTime()
            if ts > bs and ts < be:
                return (True, bre.term.duration)
            if te > bs and te < be:
                return (True, bre.term.duration)
            if ts == bs and te > be:
                return (True, bre.term.duration)
            if ts < bs and te == be:
                return (True, bre.term.duration)
        return False

    def busy(self, term: Term) -> bool:
        ts = term.getStartTime()
        te = term.getEndTime()
        for les in list(self.lesson_dict.values()):
            if term.day == les.term.day:
                ls = les.term.getStartTime()
                le = les.term.getEndTime()
                if ts > ls and ts < le:
                    return True
                if te > ls and te < le:
                    return True
                if ts == ls:
                    return True
                if te == le:
                    return True
                if ts < ls and te > le:
                    return True
                if ts > ls and te < le:
                    return True
        return False

    def put(self, lesson: Lesson) -> bool:
        if type(lesson) is not Lesson:
            raise TypeError('Argument \'put()\' musi być typu \'Lesson\'')
            return False
        else:
            for les in list(self.lesson_dict.values()):
                if les.term == lesson.term:
                    raise ValueError(f'Podany termin jest zajęty przez inną lekcję')
                    return False

            if self.overlapsBreak(lesson.term):
                raise ValueError('Podany termin jest zajęty przez przerwę')
                return False

            self.lesson_dict[f'{lesson.term.printStartTime()}-{lesson.term.printEndTime()}-{lesson.term.day}'] = lesson
            return True
        return False

    def __str__(self):
        timetab = []
        for les in list(self.lesson_dict.values()):
            tstr = f'{les.term.printStartTime()}-{les.term.printEndTime()}'
            if not tstr in timetab:
                timetab.append(tstr)

        for bre in self.breaks:
            tstr = f'{bre.term.printStartTime()}-{bre.term.printEndTime()}'
            if not tstr in timetab:
                timetab.append(tstr)

        timetab = sorted(timetab)

        disptab = []
        for i in range(8):
            disptab.append([])
            for j in range(len(timetab) + 1):
                disptab[i].append('')
        
        for d in Day:
            disptab[d.value][0] = str(d)

        for c, t in enumerate(timetab):
            disptab[0][c + 1] = f'{t}'

        for les in list(self.lesson_dict.values()):
            tstr = f'{les.term.printStartTime()}-{les.term.printEndTime()}'
            disptab[les.term.day.value][timetab.index(tstr) + 1] = les.name

        for bre in self.breaks:
            tstr = f'{bre.term.printStartTime()}-{bre.term.printEndTime()}'
            for i in range(1, 8):
                disptab[i][timetab.index(tstr) + 1] = f'------'

        b = ''
        bl = f'\n{b: ^12}{b:*^92}\n'
        em = f'{b: ^12}'

        finstr = ''
        for tc in range(len(timetab) + 1):
            for dc in range(8):
                finstr += f'{disptab[dc][tc]: ^12}*'
            finstr += bl

        return finstr

