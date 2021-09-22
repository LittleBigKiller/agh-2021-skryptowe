'''
import sys, getopt

try:
    opt, args = getopt.getopt(sys.argv[1:], 'x')
except:
    exit()

clist = []
for fn in args:
    fc = open(fn, 'r').read()
    clist.extend(fc.split())

print(len(list(filter(lambda x: int(x) % 2 == 0, clist))))
'''

from functools import reduce;
import re, sys;

print(
        len(
            list(
                filter( lambda x: int(x) % 2 == 0,
                    list(
                        re.findall( r'\d+',
                            reduce( lambda x, y: x + y,
                                list(
                                    map( lambda x: open(x, 'r').read(), sys.argv[1:])
                                )
                            )
                        )
                    )
                )
            )
        )
)

