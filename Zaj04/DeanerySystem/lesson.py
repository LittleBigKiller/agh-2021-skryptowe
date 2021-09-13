from .day import Day
from .term import Term

class Lesson():
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        if self.term.getDay().value < 5:
            self.full_time = True
        elif self.term.getDay().value > 5:
            self.full_time = False
        else:
            if self.term.hour < 17:
                self.full_time = True
            else:
                self.full_time = False

    def earlierDay(self):
        ndv = self.term.getDay().value - 1

        if self.full_time and ndv < 1:
            return False
        elif not self.full_time and ndv < 5:
            return False

        if not self.full_time and ndv == 5 and self.term.hour < 17:
            return False

        new_day = Day(ndv)
        self.term.setDay(new_day)
        return True

    def laterDay(self):
        ndv = self.term.getDay().value + 1

        if self.full_time and ndv > 5:
            return False
        elif not self.full_time and ndv > 7:
            return False

        temp_term = Term(self.term.hour, self.term.minute, Day(ndv))
        proj_endt = temp_term.getEndTime()

        if self.full_time and ndv == 5 and proj_endt[0] >= 17:
                return False

        new_day = Day(ndv)
        self.term.setDay(new_day)
        return True

    def earlierTime(self):
        dur = self.term.duration
        h_dif = dur // 60
        m_dif = dur % 60

        if self.term.minute - m_dif < 0:
            m_dif -= 60
            h_dif += 1

        if self.term.hour - h_dif < 8:
            return False

        if self.term.getDay().value == 5 and not self.full_time and self.term.hour - h_dif < 17:
                return False

        self.term.hour -= h_dif
        self.term.minute -= m_dif
        return True

    def laterTime(self):
        dur = self.term.duration
        h_dif = dur // 60
        m_dif = dur % 60

        if self.term.minute + m_dif > 60:
            m_dif -= 60
            h_dif += 1

        temp_term = Term(self.term.hour + h_dif, self.term.minute + m_dif, Day.MON)
        proj_endt = temp_term.getEndTime()
        
        if proj_endt[0] >= 20:
            return False

        if self.term.getDay().value == 5 and self.full_time and proj_endt[0] >= 17:
                return False

        self.term.hour += h_dif
        self.term.minute += m_dif
        return True

    def __str__(self):
        if self.year == 1:
            year_str = 'Pierwszy rok'
        elif self.year == 2:
            year_str = 'Drugi rok'
        elif self.year == 3:
            year_str = 'Trzeci rok'
        elif self.year == 4:
            year_str = 'Czwarty rok'
        elif self.year == 5:
            year_str = 'Piąty rok'

        if self.full_time:
            time_str = 'stacjonarnych'
        else:
            time_str = 'niestacjonarnych'

        return (f'{self.name} ({self.term.getDay()} {self.term.printStartTime()}-{self.term.printEndTime()})\n'
                f'{year_str} studiów {time_str}\n' # Tutaj ma na podstawie dnia tygodnia decydować
                f'Prowadzący: {self.teacherName}')


