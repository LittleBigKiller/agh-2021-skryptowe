from functools import reduce
import re
import sys


# wypisujemy
print(
    # liczymy długość listy
    len(
        # rzutujemy wynik na listę
        list(
            # wybieramy tylko elementy z listy, które spełniają warunek postawiony w funkcji
            filter(
                # funkcja sprawdzająca, czy podany argument zamieniony na liczbę jest parzysty
                lambda x: int(x) % 2 == 0,
                # rzutujemy wynik na listę
                list(
                    # znajdujemy wszystkie liczby (jedna lub więcej cyfra)
                    re.findall(r'\d+',
                        # połączenie wszystkich elementów listy zgodnie z funkcją
                        reduce(
                            # funkcja składająca każde dwa podane elementy w jeden
                            lambda x, y: x + y,
                            # rzutowanie wyniku na listę
                            list(
                                # wykonananie funkcji z każdym parametrem linii komend jako argumentem
                                map(
                                    # funkcja otwierająca argument parametr jako plik i wyciągająca jego zawartość
                                    lambda x: open(x, 'r').read(),
                                    # argumenty z linii komend
                                    sys.argv[1:]
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
