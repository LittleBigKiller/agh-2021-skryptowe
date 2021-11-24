from DeanerySystem import Day, Term, Lesson, Break, BasicTerm, Timetable1, Timetable2
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class Invoker():

    def __init__(self, receiver, tt_dict):
        self.rcv = receiver
        self.tt_dict = tt_dict
        self.valid_cmd = ['p', 'd+', 'd-', 't+', 't-', 'sb+', 'sb-']

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
        if cmd == 'p':
            self.rcv.do_print(self.tt_dict[cmdtab[0]])
        elif cmd == 'd+':
            self.rcv.do_dl(self.tt_dict[cmdtab[0]])
        elif cmd == 'd-':
            self.rcv.do_de(self.tt_dict[cmdtab[0]])
        elif cmd == 't+':
            self.rcv.do_tl(self.tt_dict[cmdtab[0]])
        elif cmd == 't-':
            self.rcv.do_te(self.tt_dict[cmdtab[0]])
        elif cmd == 'sb+':
            self.rcv.do_sbt(self.tt_dict[cmdtab[0]])
        elif cmd == 'sb-':
            self.rcv.do_sbf(self.tt_dict[cmdtab[0]])
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
    inv = Invoker(rcv, tts)
    while True:
        try:
            text = input()
        except EOFError:
            break
        inv.parse_exec(text)
        
