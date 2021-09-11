from fractions import Fraction

def sum(arg1, arg2):
    if type(arg1) is complex or type(arg2) is complex:
        return complex(arg1.real + arg2.real, arg1.imag + arg2.imag)

    if type(arg1) is Fraction or type(arg2) is Fraction:
        return Fraction(arg1 + arg2)

    arg1 = float(arg1)
    arg2 = float(arg2)
    return arg1 + arg2

if __name__ == '__main__':
    print('suma = {}'.format(sum(1, 2)))
    print('__name__ = {}'.format(__name__))