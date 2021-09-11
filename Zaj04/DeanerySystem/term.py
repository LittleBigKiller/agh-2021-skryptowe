from day import Day

class Term():
    def __init__(self, hour, minute, day, duration=90):
        self.hour = hour
        self.minute = minute
        self._day = day
        self.duration = duration

    def __str__(self):
        return f'{self.hour}:{self.minute} [{self.duration}]'

    def getDay(self):
        return self._day

    def earlierThan(self, termin):
        if self._day.difference(termin.getDay()) < 0:
            return False
        if self._day.difference(termin.getDay()) == 0:
            if termin.hour < self.hour:
                return False
            if termin.hour == self.hour:
                if termin.minute <= self.minute:
                    return False
            return True
        return True

    def laterThan(self, termin):
        if self._day.difference(termin.getDay()) > 0:
            return False
        if self._day.difference(termin.getDay()) == 0:
            if termin.hour > self.hour:
                return False
            if termin.hour == self.hour:
                if termin.minute >= self.minute:
                    return False
            return True
        return True

    def equals(self, termin):
        if termin.hour == self.hour and termin.minute == self.minute and \
            termin.duration == self.duration and self._day.difference(termin.getDay()) == 0:
            return True
        return False

    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    def getEndTime(self):
        add_hour = self.duration // 60
        add_min = self.duration % 60
        end_min = self.minute + add_min

        if end_min > 60:
            add_hour += 1
            end_min %= 60

        end_hour = self.hour + add_hour

        return (end_hour, end_min)

    def printEndTime(self):
        timeTuple = self.getEndTime()
        return f'{timeTuple[0]}:{timeTuple[1]:0>2}'

    def printStartTime(self):
        return f'{self.hour}:{self.minute:0>2}'

    def __sub__(self, termin):
        add_hour = self.duration // 60
        add_min = self.duration % 60
        fin_dur = 0
        h_dif = self.hour + add_hour - termin.hour
        m_dif = self.minute + add_min - termin.minute
        fin_dur += h_dif * 60 + m_dif
        return Term(termin.hour, termin.minute, fin_dur)
