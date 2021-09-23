from inspect import signature as sig

######################
# funkcja dekorująca #
######################
# zewnętrzna część pobiera argumenty funkcji (argSuma/argRoznica)
def argumenty(pargs):
        # dec_argumenty pobiera samą funkcję dekorowaną
        def dec_argumenty(func):
            # wrap zawija się wokół dekorowanej funkcji, przekazuje wszystkie argumenty podane jej przy wywołaniu,
            # bez precyzowania 'self', żeby nie być tylko do metod klasowych (bez znaczenia tutaj)
            def wrap_argumenty(*args):
                # pobranie ilości KONIECZNYCH argumentów
                pnum = len(list(sig(func).parameters))
                # zmienna przechowująca finałową listę argumentów (przypisane do niej argumenty wywołania)
                fargs = list(args)
                # ilość podanych przy wywołaniu argumentów
                gnum = len(fargs) + len(pargs)

                # jeżeli mamy za mało podanych argumentów, żeby je uzupełnić - podnosimy TypeError
                if gnum < pnum:
                    raise TypeError(f'{func.__name__} takes exactly {pnum} arguments ({gnum} given)')
                
                # dodajemy kolejne argumenty aż finałowa lista będzie odpowiedniej długości
                ctr = 0
                while len(fargs) < pnum:
                    fargs.append(pargs[ctr])
                    ctr += 1

                # wywołujemy zawijaną funkcję z uzupełnionymi argumentami, * przed tablicą podaje tablice po jednej zmiennej
                func(*fargs)

                # próbujemy podać kolejną zmienną spośród podanych dekoratorowi
                try:
                    return pargs[ctr]
                # jeżeli nie ma już dostępnych argumentów (nie udało się), zwracamy None
                except:
                    return None

            return wrap_argumenty

        return dec_argumenty

#####################################
# klasa, której funkcje udekorujemy #
#####################################
class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    # dekorujemy po raz pierwszy funkcje w momencie definicji klasy
    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')

    # tworzymy też ich kopię bez dekoracji (żeby nie musieć jej redefiniować @ runtime, choć też można)
    def ud_suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    def ud_roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')

    # funkcja setitem oprócz ustawiania odpowiednich wartości, również refefiniuje odpowiednią funkcje dekorowaną
    def __setitem__(self, key, value):
        if key == 'suma':
            self.argumentySuma = value
            # do self.suma przypisujemy nowy obiekt udekorowanej funkcji z nowymi wartościami zmiennej klasowej podanymi dekoratorowi
            # (argumenty(self.argumentySuma)) - definicja naszej funkcji dekoracyjnej, odpowiednik @argumenty(argumentySuma)
            # (x)(func) - podanie func do naszej właśnie ewaluowanej (x), nowy obiekt funkcji
            self.suma = (argumenty(self.argumentySuma))(self.ud_suma)
        elif key == 'roznica':
            self.argumentyRoznica = value
            self.roznica = (argumenty(self.argumentyRoznica))(self.ud_roznica)

# krótkie jeszcze wyjaśnienie tych dekoracji:
# 1) @decor(par)
#    def func()
# #  ^ ten sposób oznacza zastąpienie func() jej dekorowaną wersją
#
# 2) (decor(par))(func)
# #  ^ ten sposób dekoracji tworzy nam zmienną w pamięci, którą możemy dowolnie przypisać, do innej zmiennej, lub zwyczajnie użyć i usunąć

