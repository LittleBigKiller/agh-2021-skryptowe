lista = []

# print('Ładowanie modułu "{0}"'.format(__name__))

def zapisz(arg_str):
    for char in arg_str:
        if not char.isnumeric():
            continue
        found = False
        for item in lista:
            if item[0] == char:
                found = True
                item[1] += 1
        if not found:
            lista.append([char, 1])
    lista.sort()


def wypisz():
    # print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    if lista:
        last = lista[-1][0]
        for k, v in lista:
            if k == last:
                print(f'{k}:{v}')
            else:
                print(f'{k}:{v}',end=',')


# print('Załadowano moduł "{0}"'.format(__name__))
