from day import Day, nthDayFrom

class Term():
    def __init__(self, day, hour, minute):
        self._day = day
        self.hour = hour
        self.minute = minute
        self.duration = 90

    def __str__(self):
        return f'{str(self._day)} {self.hour}:{self.minute} [{self.duration}]'

    def __repr__(self):
        return f'{str(self._day)} {self.hour}:{self.minute} [{self.duration}]'

    def getNumVal(self):
        return (self._day-1)*1440+self.hour*60+self.minute

    def getDay(self):
        return self._day

    def dayOfWeek(self, day, month, year):
        mlookup = {
            '-9': 274,
            '-8': 241,
            '-7': 213,
            '-6': 181,
            '-5': 155,
            '-4': 123,
            '-3': 90,
            '-2': 58,
            '-1': 32,
            '0': 0,
            '1': 31,
            '2': 61
            }
        kday = 29
        kmonth = 10
        kyear = 2021
        mdif = str(month-kmonth)
        day_dif = day-kday + mlookup[mdif] + (year-kyear)*365
        day_dif %= 7
        print(month-kmonth)
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
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9,
            'X': 10,
            'XI': 11,
            'XII': 12
            }
        return int(roman[string])

    def toMinutes(self, year_dif, month_dif, day_dif, hour_dif, min_dif):
        total = 0
        total += year_dif*525600
        total += month_dif*43800
        total += day_dif*1440
        total += hour_dif*60
        total += min_dif
        return total

    def setTerm(self, string):
        date_elems = string.split('-')
        for de in date_elems:
            de.rstrip()
        date_elems = ''.join(date_elems)
        date1 = date_elems.split(' ')[:4]
        date2 = date_elems.split(' ')[5:]

        ndur = self.toMinutes(
                int(date2[2]) - int(date1[2]),
                self.toRoman(date2[1]) - self.toRoman(date1[1]),
                int(date2[0]) - int(date1[0]),
                int(date2[3].split(':')[0]) - int(date1[3].split(':')[0]),
                int(date2[3].split(':')[1]) - int(date1[3].split(':')[1])
                )
        nday = self.dayOfWeek(
            int(date1[0]),
            self.toRoman(date1[1]),
            int(date1[2])
            )

        self._day = nday
        self.hour = date1[3].split(':')[0]
        self.minute = date1[3].split(':')[1]
        self.duration = ndur


