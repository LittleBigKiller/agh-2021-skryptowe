slownik = {}

# print('Ładowanie modułu "{0}"'.format(__name__))

def zapisz(arg_str):
    for char in arg_str:
        if not char.isnumeric():
            continue
        if char in slownik.keys():
            slownik[char] += 1
        else:
            slownik[char] = 1


def wypisz():
    # print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    if slownik:
        last = sorted(slownik.keys())[-1]
        for k, v in sorted(slownik.items()):
            if k == last:
                print(f'{k}:{v}')
            else:
                print(f'{k}:{v}',end=',')


# print('Załadowano moduł "{0}"'.format(__name__))