from .day import Day, nthDayFrom


class Term():
    def __init__(self, day, hour, minute):
        self._day = day
        self.hour = hour
        self.minute = minute
        self.duration = 90

    def __str__(self):
        return f'{repr(self._day)} {self.hour}:{self.minute} [{self.duration}]'

    def __repr__(self):
        return f'{repr(self._day)} {self.hour}:{self.minute} [{self.duration}]'

    def getNumVal(self):
        return (self._day-1)*1440+self.hour*60+self.minute

    def getDay(self):
        return self._day

    def dayOfWeek(self, day, month, year):
        moffset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        kday = 1
        kmonth = 1
        kyear = 2021

        ddif = day - kday
        mdif = month - kmonth
        ydif = year - kyear

        day_dif = ddif + moffset[mdif] + ydif * 365
        day_dif %= 7

        return nthDayFrom(day_dif, Day.FRI)

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

    def toRoman(self, string):
        roman = {
            'I': 1,     'II': 2,    'III': 3,   'IV': 4,
            'V': 5,     'VI': 6,    'VII': 7,   'VIII': 8,
            'IX': 9,    'X': 10,    'XI': 11,   'XII': 12
        }
        return int(roman[string])

    def toMinutes(self, day_dif, month_dif, year_dif, hour_dif, min_dif):
        total = 0
        total += year_dif * 525600
        total += month_dif * 43800
        total += day_dif * 1440
        total += hour_dif * 60
        total += min_dif
        return total

    def setTerm(self, string):
        date_elems = string.split(' ')
        date1 = date_elems[:4]
        date2 = date_elems[5:]

        d1day = int(date1[0])
        d1mon = self.toRoman(date1[1])
        d1yea = int(date1[2])
        d1hou = int(date1[3].split(':')[0])
        d1min = int(date1[3].split(':')[1])

        d2day = int(date2[0])
        d2mon = self.toRoman(date2[1])
        d2yea = int(date2[2])
        d2hou = int(date2[3].split(':')[0])
        d2min = int(date2[3].split(':')[1])

        ndur = self.toMinutes(
            d2day - d1day,
            d2mon - d1mon,
            d2yea - d1yea,
            d2hou - d1hou,
            d2min - d1min
        )
        nday = self.dayOfWeek(d1day, d1mon, d1yea)

        self._day = nday
        self.hour = date1[3].split(':')[0]
        self.minute = date1[3].split(':')[1]
        self.duration = ndur
