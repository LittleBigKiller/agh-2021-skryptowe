import sys
import getopt

from typy import lista, slownik


arg_str = ''.join(sys.argv[2:])

if sys.argv[1] == '--lista':
    lista.zapisz(arg_str)
    lista.wypisz()
elif sys.argv[1] == '--slownik':
    slownik.zapisz(arg_str)
    slownik.wypisz()
else:
    print('Nieprawidłowy pierwszy argument, spróbuj \'--lista\' lub \'--slownik\'')