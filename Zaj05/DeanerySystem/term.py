from .day import Day
from .basicterm import BasicTerm

class Term(BasicTerm):
    def __init__(self, hour, minute, day, duration=90):
        super().__init__(hour, minute, duration)
        self._day = day

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError('Dzień musi być typu \'Day\'')
        else:
            self._day = value

    def earlierThan(self, termin):
        if self._day.difference(termin.day) < 0:
            return False
        if self._day.difference(termin.day) == 0:
            if termin.hour < self._hour:
                return False
            if termin.hour == self._hour:
                if termin.minute <= self._minute:
                    return False
            return True
        return True

    def laterThan(self, termin):
        if self._day.difference(termin.day) > 0:
            return False
        if self._day.difference(termin.day) == 0:
            if termin.hour > self._hour:
                return False
            if termin.hour == self._hour:
                if termin.minute >= self._minute:
                    return False
            return True
        return True

    def equals(self, termin):
        if termin.hour == self._hour and termin.minute == self._minute and \
            termin.duration == self._duration and self._day.difference(termin.day) == 0:
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

