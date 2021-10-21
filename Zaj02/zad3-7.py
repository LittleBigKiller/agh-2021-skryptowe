import sys
import getopt

import lista, slownik

if len(sys.argv) > 1:
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
else:
    print('Skrypt wymaga argumentów do działania')