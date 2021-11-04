from typing import List

from .day import Day
from .term import Term
from .lesson import Lesson
from .action import Action


class Timetable1:
    """ Class containing a set of operations to manage the timetable """

    def __init__(self):
        self.lesson_list = []

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        """
        Informs whether a lesson can be transferred to the given term

        Parameters
        ----------
        term : Term
            The term checked for the transferability
        full_time : bool
            Full-time or part-time studies

        Returns
        -------
        bool
            **True** if the lesson can be transferred to this term
        """

        if term.hour < 8:
            return False

        et = term.getEndTime()
        if et[0] > 20:
            return False
        if et[0] == 20 and et[1] > 0:
            return False

        if not self.busy(term):
            if term.day.value < 5:
                is_ft = True
            elif term.day.value > 5:
                is_ft = False
            else:
                if term.hour < 17:
                    is_ft = True
                else:
                    is_ft = False

            if is_ft == full_time:
                return True
        return False

    def busy(self, term: Term) -> bool:
        """
        Informs whether the given term is busy.  Should not be confused with ``can_be_transfered_to()``
        since there might be free term where the lesson cannot be transferred.

        Parameters
        ----------
        term : Term
            Checked term

        Returns
        -------
        bool
            **True** if the term is busy
        """

        for les in self.lesson_list:
            if les.term == term:
                return True

            les_start = (les.term.hour, les.term.minute)
            les_end = les.term.getEndTime()
            ter_start = (term.hour, term.minute)
            ter_end = term.getEndTime()

            if les_end > ter_start and les_end < ter_end:
                return True
            if ter_end > les_start and ter_end < les_end:
                return True
            if les_start > ter_start and les_start < ter_end:
                return True
            if ter_start > les_start and ter_start < les_end:
                return True

        return False

    def put(self, lesson: Lesson) -> bool:
        """
        Add the given lesson to the timetable.

        Parameters
        ----------
        lesson : Lesson
            The added  lesson

        Returns
        -------
        bool
            **True**  if the lesson was added.  The lesson cannot be placed if the timetable slot is already occupied.
        """

        if type(lesson) is not Lesson:
            raise TypeError('Argument \'put()\' musi być typu \'Lesson\'')
            return False
        else:
            if self.busy(lesson.term):
                return False
            self.lesson_list.append(lesson)
            return True
        return False


    def parse(self, actions: List[str]) -> List[Action]:
        """
        Converts an array of strings to an array of 'Action' objects.

        Parameters
        ----------
        actions:  List[str]
            A list containing the strings: "d-", "d+", "t-" or "t+"

        Returns
        -------
            List[Action]
                A list containing the values:  DAY_EARLIER, DAY_LATER, TIME_EARLIER or TIME_LATER
        """

        action_list = []
        for ac in actions:
            if ac in Action._value2member_map_:
                action_list.append(Action(ac))
        return action_list

    def perform(self, actions: List[Action]):
        """
        Transfer the lessons included in the timetable as described in the list of actions. N-th action should be sent the n-th lesson in the timetable.

        Parameters
        ----------
        actions : List[Action]
            Actions to be performed
        """
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

    def __str__(self):
        timetab = []
        for les in self.lesson_list:
            timetab.append(les.term)
        timetab = sorted(timetab, key=lambda t: t.printStartTime())

        disptab = []
        for i in range(8):
            disptab.append([])
            for j in range(len(timetab) + 1):
                disptab[i].append('')
        
        for d in Day:
            disptab[d.value][0] = str(d)

        for c, t in enumerate(timetab):
            disptab[0][c + 1] = f'{t.printStartTime()}-{t.printEndTime()}'

        for les in self.lesson_list:
            disptab[les.term.day.value][timetab.index(les.term) + 1] = les.name

        b = ''
        bl = f'\n{b: ^12}{b:*^92}\n'
        em = f'{b: ^12}'

        finstr = ''
        for tc in range(len(timetab) + 1):
            for dc in range(8):
                finstr += f'{disptab[dc][tc]: ^12}*'
            finstr += bl

        return finstr
        

    def get(self, term: Term) -> Lesson:
        """
        Get object (lesson) indicated by the given term.

        Parameters
        ----------
        term: Term
            Lesson date

        Returns
        -------
        lesson: Lesson
            The lesson object or None if the term is free
        """
        
        ltr = None
        for les in self.lesson_list:
            if les.term == term:
                ltr = les
                break
        return ltr

