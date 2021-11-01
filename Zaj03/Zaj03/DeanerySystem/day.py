from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def __str__(self):
        if self.value == 1:
            day_name = 'Poniedziałek'
        elif self.value == 2:
            day_name = 'Wtorek'
        elif self.value == 3:
            day_name = 'Środa'
        elif self.value == 4:
            day_name = 'Czwartek'
        elif self.value == 5:
            day_name = 'Piątek'
        elif self.value == 6:
            day_name = 'Sobota'
        elif self.value == 7:
            day_name = 'Niedziela'

        return day_name

    def __repr__(self):
        return self.__str__()

    def difference(self, day):
        diff = day.value - self.value
        return diff + 7 if diff < -3 else (diff - 7 if diff > 3 else diff)

def nthDayFrom(n, day):
    new_day = day.value + n
    return Day(new_day + 7) if new_day < 1 else (Day(new_day - 7) if new_day > 7 else Day(new_day))
