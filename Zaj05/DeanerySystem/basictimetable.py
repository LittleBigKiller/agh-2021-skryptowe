
from typing import List

from .day import Day
from .term import Term
from .lesson import Lesson
from .action import Action


class BasicTimetable:

    def __init__(self):
        self.lesson_list = []
    
    def put(self, lesson: Lesson) -> bool:
        if type(lesson) is not Lesson:
            raise TypeError('Argument \'put()\' musi być typu \'Lesson\'')
            return False
        else:
            for les in self.lesson_list:
                if les.term == lesson.term:
                    raise ValueError(f'Podany termin jest zajęty')
                    return False
            self.lesson_list.append(lesson)
            return True
        raise ValueError(f'Podany termin jest zajęty')
        return False


    def parse(self, actions: List[str]) -> List[Action]:
        action_list = []
        for ac in actions:
            if ac == 'd-':
                action_list.append(Action.DAY_EARLIER)
            elif ac == 'd+':
                action_list.append(Action.DAY_LATER)
            elif ac == 't-':
                action_list.append(Action.TIME_EARLIER)
            elif ac == 't+':
                action_list.append(Action.TIME_LATER)
            else:
                raise ValueError(f'Translacja {ac} jest niepoprawna')
        return action_list

    def perform(self, actions: List[Action]):
        lc = 0
        for ac in actions:
            if ac == Action.DAY_EARLIER:
                self.lesson_list[lc].earlierDay()
            elif ac == Action.DAY_LATER:
                self.lesson_list[lc].laterDay()
            elif ac == Action.TIME_EARLIER:
                self.lesson_list[lc].earlierTime()
            elif ac == Action.TIME_LATER:
                self.lesson_list[lc].laterTime()

            lc += 1
            lc %= len(self.lesson_list)

    def get(self, term: Term) -> Lesson:
        ltr = None
        for les in self.lesson_list:
            if les.term == term:
                ltr = les
                break
        return ltr

