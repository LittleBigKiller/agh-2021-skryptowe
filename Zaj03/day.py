from enum import Enum

class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

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