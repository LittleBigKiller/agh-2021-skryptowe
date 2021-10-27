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
        return diff + 7 if diff < -3 else (diff - 7 if diff > 3 else diff)

def nthDayFrom(n, day):
    new_day = day.value + n
    return Day(new_day + 7) if new_day < 1 else (Day(new_day - 7) if new_day > 7 else Day(new_day))