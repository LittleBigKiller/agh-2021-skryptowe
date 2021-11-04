from .day import Day

class Term():
    def __init__(self, hour, minute, day, duration=90):
        self.__hour = hour
        self.__minute = minute
        self.__day = day
        self.__duration = duration

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if type(value) is not int:
            raise TypeError('Godzina musi być liczbą całkowitą')
        elif value < 0 or value > 23:
            raise ValueError('Godzina musi należeć do przedziału 0 - 23')
        else:
            self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if type(value) is not int:
            raise TypeError('Minuta musi być liczbą całkowitą')
        elif value < 0 or value > 59:
            raise ValueError('Minuta musi należeć do przedziału 0 - 59')
        else:
            self.__minute = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if type(value) is not Day:
            raise TypeError('Dzień musi być typu \'Day\'')
        else:
            self.__day = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if type(value) is not int:
            raise TypeError('Duration musi być liczbą całkowitą')
        elif value <=0:
            raise ValueError('Duration musi być dodatnie')
        else:
            self.__duration = value

    def __str__(self):
        return f'{self.__hour}:{self.__minute} [{self.__duration}]'

    def earlierThan(self, termin):
        if self.__day.difference(termin.day) < 0:
            return False
        if self.__day.difference(termin.day) == 0:
            if termin.hour < self.__hour:
                return False
            if termin.hour == self.__hour:
                if termin.minute <= self.__minute:
                    return False
            return True
        return True

    def laterThan(self, termin):
        if self.__day.difference(termin.day) > 0:
            return False
        if self.__day.difference(termin.day) == 0:
            if termin.hour > self.__hour:
                return False
            if termin.hour == self.__hour:
                if termin.minute >= self.__minute:
                    return False
            return True
        return True

    def equals(self, termin):
        if termin.hour == self.__hour and termin.minute == self.__minute and \
            termin.duration == self.__duration and self.__day.difference(termin.day) == 0:
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
        add_hour = self.__duration // 60
        add_min = self.__duration % 60
        end_min = self.__minute + add_min

        if end_min >= 60:
            add_hour += 1
            end_min %= 60

        end_hour = self.__hour + add_hour

        return (end_hour, end_min)

    def printEndTime(self):
        timeTuple = self.getEndTime()
        return f'{timeTuple[0]:0>2}:{timeTuple[1]:0>2}'

    def printStartTime(self):
        return f'{self.__hour:0>2}:{self.__minute:0>2}'

    def __sub__(self, termin):
        add_hour = self.__duration // 60
        add_min = self.__duration % 60
        fin_dur = 0
        h_dif = self.__hour + add_hour - termin.hour
        m_dif = self.__minute + add_min - termin.minute
        fin_dur += h_dif * 60 + m_dif
        return Term(termin.hour, termin.minute, fin_dur)
