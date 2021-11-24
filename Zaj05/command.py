from DeanerySystem import Day, Term, Lesson, Break, BasicTerm, Timetable1, Timetable2
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class PrintCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_print(tt)


class DayPlusCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_dl(tt)


class DayMinusCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_de(tt)


class TimePlusCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_tl(tt)


class TimeMinusCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_te(tt)


class SkipPlusCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_sbt(tt)


class SkipMinusCommand(Command):

    def __init__(self, rcv):
        self.rcv = rcv

    def execute(self, tt):
        self.rcv.do_sbf(tt)


class Invoker():

    _on_print = None
    _on_day_plus = None
    _on_day_minus = None
    _on_time_plus = None
    _on_time_minus = None
    _on_skip_plus = None
    _on_skip_minus = None

    def __init__(self, tt_dict):
        self.tt_dict = tt_dict
        self.valid_cmd = ['p', 'd+', 'd-', 't+', 't-', 'sb+', 'sb-']

    def set_on_print(self, command):
        self._on_print = command

    def set_on_day_plus(self, command):
        self._on_day_plus = command

    def set_on_day_minus(self, command):
        self._on_day_minus = command

    def set_on_time_plus(self, command):
        self._on_time_plus = command

    def set_on_time_minus(self, command):
        self._on_time_minus = command

    def set_on_skip_plus(self, command):
        self._on_skip_plus = command

    def set_on_skip_minus(self, command):
        self._on_skip_minus = command

    def parse_exec(self, cmdstr):
        cmdtab = cmdstr.split()
        if len(cmdtab) < 2:
            print('Za krótka komenda')
            return False
        elif cmdtab[0] == 'dict':
            print(self.tt_dict)
            return True
        elif cmdtab[0] not in self.tt_dict.keys():
            print('Nie ma takiego słownika')
            return False
        elif cmdtab[1] not in self.valid_cmd:
            print('Niepoprawna komenda')
            return False
        
        cmd = cmdtab[1]
        tt = self.tt_dict[cmdtab[0]]
        if cmd == 'p':
            if isinstance(self._on_print, Command):
                self._on_print.execute(tt)
        elif cmd == 'd+':
            if isinstance(self._on_day_plus, Command):
                self._on_day_plus.execute(tt)
        elif cmd == 'd-':
            if isinstance(self._on_day_minus, Command):
                self._on_day_minus.execute(tt)
        elif cmd == 't+':
            if isinstance(self._on_time_plus, Command):
                self._on_time_plus.execute(tt)
        elif cmd == 't-':
            if isinstance(self._on_time_minus, Command):
                self._on_time_minus.execute(tt)
        elif cmd == 'sb+':
            if isinstance(self._on_skip_plus, Command):
                self._on_skip_plus.execute(tt)
        elif cmd == 'sb-':
            if isinstance(self._on_skip_minus, Command):
                self._on_skip_minus.execute(tt)
        return True


class Receiver:

    def do_print(self, tt):
        print(tt)

    def do_dl(self, tt):
        ac = tt.parse(['d+'])
        tt.perform(ac)

    def do_de(self, tt):
        ac = tt.parse(['d-'])
        tt.perform(ac)

    def do_tl(self, tt):
        ac = tt.parse(['t+'])
        tt.perform(ac)

    def do_te(self, tt):
        ac = tt.parse(['t-'])
        tt.perform(ac)

    def do_sbt(self, tt):
        if type(tt) == Timetable2:
            tt.skipBreaks = True

    def do_sbf(self, tt):
        if type(tt) == Timetable2:
            tt.skipBreaks = False


if __name__ == '__main__':
    rcv = Receiver()

    bl = [Break(BasicTerm(9, 30, 5)), Break(BasicTerm(11, 5, 10))]
    tt1 = Timetable1()
    tt2 = Timetable2(bl)
    ter1 = Term(8, 0, Day.WED)
    ter2 = Term(9, 35, Day.THU)
    les1 = Lesson(tt1, ter1, 'less1', 'less1', 2)
    les2 = Lesson(tt2, ter2, 'less2', 'less2', 2)
    tt1.put(les1)
    tt2.put(les2)
    tts = {'tt1': tt1, 'tt2': tt2}

    inv = Invoker(tts)
    inv.set_on_print(PrintCommand(rcv))
    inv.set_on_day_plus(DayPlusCommand(rcv))
    inv.set_on_day_minus(DayMinusCommand(rcv))
    inv.set_on_time_plus(TimePlusCommand(rcv))
    inv.set_on_time_minus(TimeMinusCommand(rcv))
    inv.set_on_skip_plus(SkipPlusCommand(rcv))
    inv.set_on_skip_minus(SkipMinusCommand(rcv))

    while True:
        try:
            text = input()
        except EOFError:
            break
        inv.parse_exec(text)
        

