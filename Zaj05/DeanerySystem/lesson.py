from DeanerySystem.day import Day
from DeanerySystem.term import Term


class Lesson():
    def __init__(self, timetable, term, name, teacherName, year):
        self.__timetable = timetable
        self.__term = term
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        self.__full_time = self.calcFTValue()

    def calcFTValue(self):
        if self.__term.day.value < 5:
            return True
        elif self.__term.day.value > 5:
            return False

        if self.__term.hour < 17:
            return True
        else:
            return False

    @property
    def timetable(self):
        return self.__timetable

    @timetable.setter
    def term(self, value):
        if type(value) is not Timetable1:
            raise TypeError('timetable musi być typu \'Timetable1\'')
        else:
            self.__timetable = value

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        if type(value) is not Term:
            raise TypeError('term musi być typu \'Term\'')
        else:
            self.__term = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name musi być typu \'str\'')
        else:
            self.__term = value

    @property
    def teacherName(self):
        return self.__teacherName

    @teacherName.setter
    def teacherName(self, value):
        if type(value) is not str:
            raise TypeError('teacherName musi być typu \'str\'')
        else:
            self.__teacherName = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if type(value) is not int:
            raise TypeError('rok musi być liczbą całkowitą')
        elif value <= 0:
            raise ValueError('rok musi być liczbą dodatnią')
        else:
            self.__year = value

    @property
    def full_time(self):
        return self.__full_time

    def earlierDay(self):
        ndv = self.__term.day.value - 1

        if ndv < 1:
            return False

        nd = Day(ndv)
        nt = Term(self.__term.hour, self.__term.minute, nd)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self.__term.day = nd
        return True

    def laterDay(self):
        ndv = self.__term.day.value + 1

        if ndv > 7:
            return False

        nd = Day(ndv)
        nt = Term(self.__term.hour, self.__term.minute, nd)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self.__term.day = nd
        return True

    def earlierTime(self):
        h_dif = self.__term.duration // 60
        m_dif = self.__term.duration % 60

        if self.__term.minute - m_dif < 0:
            m_dif -= 60
            h_dif += 1

        nt = Term(self.__term.hour - h_dif,
                  self.__term.minute - m_dif, self.__term.day)

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

                    if self.__term.minute - m_dif < 0:
                        m_dif -= 60
                        h_dif += 1

                    nt = Term(self.__term.hour - h_dif,
                              self.__term.minute - m_dif, self.__term.day)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self.__term.hour -= h_dif
        self.__term.minute -= m_dif
        return True

    def laterTime(self):
        h_dif = self.__term.duration // 60
        m_dif = self.__term.duration % 60

        if self.__term.minute + m_dif >= 60:
            m_dif -= 60
            h_dif += 1

        nt = Term(self.__term.hour + h_dif,
                  self.__term.minute + m_dif, self.__term.day)

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

                    if self.__term.minute + m_dif > 60:
                        m_dif -= 60
                        h_dif += 1

                    nt = Term(self.__term.hour + h_dif,
                              self.__term.minute + m_dif, self.__term.day)

        if not self.timetable.can_be_transferred_to(nt, self.full_time):
            return False

        self.__term.hour += h_dif
        self.__term.minute += m_dif
        return True

    def __str__(self):
        if self.__year == 1:
            year_str = 'Pierwszy rok'
        elif self.__year == 2:
            year_str = 'Drugi rok'
        elif self.__year == 3:
            year_str = 'Trzeci rok'
        elif self.__year == 4:
            year_str = 'Czwarty rok'
        elif self.__year == 5:
            year_str = 'Piąty rok'

        if self.__full_time:
            time_str = 'stacjonarnych'
        else:
            time_str = 'niestacjonarnych'

        return (f'{self.__name} ({self.__term.day} {self.__term.printStartTime()}-{self.__term.printEndTime()})\n'
                f'{year_str} studiów {time_str}\n'
                f'Prowadzący: {self.__teacherName}')
                
from DeanerySystem.timetable1 import Timetable1
from DeanerySystem.timetable2 import Timetable2