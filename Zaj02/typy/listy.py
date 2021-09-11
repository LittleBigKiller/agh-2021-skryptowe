from typy import lista

def zapisz(arg_str):
    global lista
    for char in arg_str:
        found = False
        for item in lista:
            if item[0] == char:
                found = True
                item[1] += 1
        if not found:
            lista.append([char, 1])
    lista.sort()

        

def wypisz():
    global lista
    last = lista[-1][0]
    for k, v in lista:
        if k == last:
            print(f'{k}:{v}')
        else:
            print(f'{k}:{v}',end=',')
