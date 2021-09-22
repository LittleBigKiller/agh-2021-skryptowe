from inspect import signature as sig

class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def argumenty(pargs):
        def dec_argumenty(func):
            def wrap_argumenty(*args):
                pnum = len(list(sig(func).parameters))
                fargs = list(args)
                gnum = len(fargs) + len(pargs)

                if gnum < pnum:
                    print('ZA MAŁO - {len(fargs) + len(pargs)}')
                    raise TypeError(f'{func.__name__} takes exactly {pnum} arguments ({gnum} given)')
                
                ctr = 0
                while len(fargs) < pnum:
                    fargs.append(pargs[ctr])
                    ctr += 1

                func(*fargs)

                try:
                    return pargs[ctr]
                except:
                    return None
            return wrap_argumenty
        return dec_argumenty

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    def ud_suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')


    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')

    def ud_roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')

    def __setitem__(self, key, value):
        if key == 'suma':
            self.argumentySuma = value
        elif key == 'roznica':
            self.argumentyRoznica = value

        def n_argumenty(pargs):
            def dec_argumenty(func):
                def wrap_argumenty(*args):
                    pnum = len(list(sig(func).parameters))
                    fargs = list(args)
                    gnum = len(fargs) + len(pargs)

                    if gnum < pnum:
                        raise TypeError(f'{func.__name__} takes exactly {pnum} arguments ({gnum} given)')
                    
                    ctr = 0
                    while len(fargs) < pnum:
                        fargs.append(pargs[ctr])
                        ctr += 1

                    func(*fargs)

                    try:
                        return pargs[ctr]
                    except:
                        return None
                return wrap_argumenty
            return dec_argumenty

        self.suma = (n_argumenty(self.argumentySuma))(self.ud_suma)
        self.roznica = (n_argumenty(self.argumentyRoznica))(self.ud_roznica)

