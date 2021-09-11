import sys
import getopt

import typy

# arg_str = ''.join(sys.argv[2:])
# 
# if sys.argv[1] == '--lista':
#     listy.zapisz(arg_str)
#     listy.wypisz()
# elif sys.argv[1] == '--slownik':
#     slowniki.zapisz(arg_str)
#     slowniki.wypisz()
# else:
#     print('Nieprawidłowy pierwszy argument, spróbuj \'--lista\' lub \'--slownik\'')


try:
    opt, args = getopt.getopt(sys.argv[1:], 'x', ['method='])
except:
    print('Nieprawidłowy pierwszy argument, spróbuj \'--method=lista\' lub \'--method=slownik\'')

args = ''.join(args)

if opt[0][1] == 'lista':
    typy.listy.zapisz(args)
    typy.listy.wypisz()
elif opt[0][1] == 'slownik':
    typy.slowniki.zapisz(args)
    typy.slowniki.wypisz()