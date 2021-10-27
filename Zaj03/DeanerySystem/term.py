from day import Day

class Term():
    def __init__(self, day, hour, minute):
        self._day = day
        self.hour = hour
        self.minute = minute
        self.duration = 90

    def __str__(self):
        return f'{self._day} {self.hour}:{self.minute} [{self.duration}]'

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
