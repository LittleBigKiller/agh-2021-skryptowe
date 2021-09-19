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

    def difference(self, day):
        diff = day.value - self.value
        if diff > 3:
            diff -= 7
        if diff < -3:
            diff += 7
        return diff

def nthDayFrom(n, day):
    new_day = day.value + n
    if new_day < 1:
        new_day += 7
    elif new_day > 7:
        new_day -= 7
    return Day(new_day)