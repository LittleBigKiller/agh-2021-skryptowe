import sys

uin = sysuin = sys.stdin.readlines()

sub_dict = {}
chan_dict = {}

def print_user(uname):
    if line[1] in sub_dict:
        print(f'{line[1]} is subbed to:')
        for chid in sub_dict[line[1]]:
            print(f'{chid}: {", ".join(chan_dict[chid])}')
        return sub_dict[line[1]]
    return None

def sub(uname, chid):
    if line[1] not in sub_dict:
        sub_dict[line[1]] = []
    if line[2] in chan_dict:
        sub_dict[line[1]].append(line[2])
    return sub_dict

def unsub(uname, chid):
    if line[1] not in sub_dict:
        return sub_dict
    if line[2] in chan_dict:
        try:
            sub_dict[line[1]].remove(line[2])
        except:
            return sub_dict
    return sub_dict

def add(chid, title):
    if line[1] in chan_dict:
        chan_dict[line[1]].append(line[2])
    else:
        chan_dict[line[1]] = [line[2]]
    return chan_dict

def rem(chid, title):
    if line[1] in chan_dict:
        try:
            chan_dict[line[1]].remove(line[2])
        except:
            return chan_dict
    else:
        return chan_dict
    return chan_dict

if __name__ == '__main__':
    for line in uin:
        line = line.split()
        if len(line) == 2:
            if line[0] == 'print':
                print_user(line[1])
        elif len(line) == 3:
            if line[0] == 'add':
                add(line[1], line[2])
            elif line[0] == 'rem':
                rem(line[1], line[2])
            if line[0] == 'sub':
                sub(line[1], line[2])
            elif line[0] == 'unsub':
                unsub(line[1], line[2])

