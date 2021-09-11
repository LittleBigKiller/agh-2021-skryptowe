from day import Day
from term import Term

class Lesson():
    def __init__(self, term, name, teacherName, year):
        self.term = term
        self.name = name
        self.teacherName = teacherName
        self.year = year
        self.full_time = False

    def earlierDay(self, days):
        return True

    def laterDay(self, days):
        return True

    def earlierTime(self):
        return True

    def laterTime(self):
        return True

    def __str__(self):
        return (f'{self.name} ({self.term.getDay()} {self.term.printStartTime()}-{self.term.printEndTime()})\n'
                f'Drugi rok studiów stacjonarnych\n' # Tutaj ma na podstawie dnia tygodnia decydować
                f'Prowadzący: {self.teacherName}')


