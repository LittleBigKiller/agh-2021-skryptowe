import sys
import getopt

from typy import lista, slownik

try:
    opt, args = getopt.getopt(sys.argv[1:], '', ['modul='])

    args = ''.join(args)

    if opt[0][1] == 'lista':
        lista.zapisz(args)
        lista.wypisz()
    elif opt[0][1] == 'slownik':
        slownik.zapisz(args)
        slownik.wypisz()
except:
    print('Nieprawidłowy pierwszy argument, spróbuj \'--modul=lista\' lub \'--modul=slownik\'')