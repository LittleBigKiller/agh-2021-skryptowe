from .day import Day
from .term import Term

class Lesson():
    def __init__(self, timetable, term, name, teacherName, year):
        self._timetable = timetable
        self._term = term
        self._name = name
        self._teacherName = teacherName
        self._year = year
        self._full_time = self.calcFTValue()

    def calcFTValue(self):
        if self._term.day.value < 5:
            return True
        elif self._term.day.value > 5:
            return False
        
        if self._term.hour < 17:
            return True
        else:
            return False

    @property
    def timetable(self):
        return self._timetable

    @timetable.setter
    def term(self, value):
        if type(value) is not Timetable1:
            raise TypeError('timetable musi być typu \'Timetable1\'')
        else:
            self._timetable = value

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        if type(value) is not Term:
            raise TypeError('term musi być typu \'Term\'')
        else:
            self._term = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name musi być typu \'str\'')
        else:
            self._term = value

    @property
    def teacherName(self):
        return self._teacherName

    @teacherName.setter
    def teacherName(self, value):
        if type(value) is not str:
            raise TypeError('teacherName musi być typu \'str\'')
        else:
            self._teacherName = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if type(value) is not int:
            raise TypeError('rok musi być liczbą całkowitą')
        elif value <= 0:
            raise ValueError('rok musi być liczbą dodatnią')
        else:
            self._year = value

    @property
    def full_time(self):
        return self._full_time

    def earlierDay(self):
        ndv = self._term.day.value - 1

        if ndv < 1:
            return False

        nd = Day(ndv)
        nt = Term(self._term.hour, self._term.minute, nd)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self._term.day = nd 
        return True

    def laterDay(self):
        ndv = self._term.day.value + 1

        if ndv > 7:
            return False

        nd = Day(ndv)
        nt = Term(self._term.hour, self._term.minute, nd)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self._term.day = nd
        return True

    def earlierTime(self):
        h_dif = self._term.duration // 60
        m_dif = self._term.duration % 60

        if self._term.minute - m_dif < 0:
            m_dif -= 60
            h_dif += 1

        nt = Term(self._term.hour - h_dif, self._term.minute - m_dif, self._term.day)
        
        if hasattr(self.timetable, 'breaks'):
            if not self.timetable.skipBreaks:
                bo = self.timetable.overlapsBreak(nt)
                if bo:
                    return False
            else:
                bo = self.timetable.overlapsBreak(nt)
                if bo:
                    h_dif += bo[1] // 60
                    m_dif += bo[1] % 60

                    if self._term.minute - m_dif < 0:
                        m_dif -= 60
                        h_dif += 1

                    nt = Term(self._term.hour - h_dif, self._term.minute - m_dif, self._term.day)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self._term.hour -= h_dif
        self._term.minute -= m_dif
        return True

    def laterTime(self):
        h_dif = self._term.duration // 60
        m_dif = self._term.duration % 60

        if self._term.minute + m_dif >= 60:
            m_dif -= 60
            h_dif += 1

        nt = Term(self._term.hour + h_dif, self._term.minute + m_dif, self._term.day)

        if hasattr(self.timetable, 'breaks'):
            if not self.timetable.skipBreaks:
                bo = self.timetable.overlapsBreak(nt)
                if bo:
                    return False
            else:
                bo = self.timetable.overlapsBreak(nt)
                if bo:
                    h_dif += bo[1] // 60
                    m_dif += bo[1] % 60

                    if self._term.minute - m_dif < 0:
                        m_dif -= 60
                        h_dif += 1

                    nt = Term(self._term.hour - h_dif, self._term.minute - m_dif, self._term.day)



        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self._term.hour += h_dif
        self._term.minute += m_dif
        return True

    def __str__(self):
        if self._year == 1:
            year_str = 'Pierwszy rok'
        elif self._year == 2:
            year_str = 'Drugi rok'
        elif self._year == 3:
            year_str = 'Trzeci rok'
        elif self._year == 4:
            year_str = 'Czwarty rok'
        elif self._year == 5:
            year_str = 'Piąty rok'

        if self._full_time:
            time_str = 'stacjonarnych'
        else:
            time_str = 'niestacjonarnych'

        return (f'{self._name} ({self._term.day} {self._term.printStartTime()}-{self._term.printEndTime()})\n'
                f'{year_str} studiów {time_str}\n'
                f'Prowadzący: {self._teacherName}')

from .timetable1 import Timetable1
from .timetable2 import Timetable2
