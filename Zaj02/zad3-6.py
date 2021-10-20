import sys
import getopt

import lista, slownik

if sys.argv:
    arg_str = ''.join(sys.argv[2:])

    if sys.argv[1] == '--lista':
        lista.zapisz(arg_str)
        lista.wypisz()
    elif sys.argv[1] == '--slownik':
        slownik.zapisz(arg_str)
        slownik.wypisz()
    else:
        print('Nieprawidłowy pierwszy argument, spróbuj \'--lista\' lub \'--slownik\'')
else:
    print('Skrypt wymaga argumentów do działania')