from typy import slownik

def zapisz(arg_str):
    global slownik
    for char in arg_str:
        if char in slownik.keys():
            slownik[char] += 1
        else:
            slownik[char] = 1

def wypisz():
    global slownik
    last = sorted(slownik.keys())[-1]
    for k, v in sorted(slownik.items()):
        if k == last:
            print(f'{k}:{v}')
        else:
            print(f'{k}:{v}',end=',')