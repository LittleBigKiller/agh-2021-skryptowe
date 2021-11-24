import sys
from collections import Counter


# wypisujemy na ekran
print(
    # tworzymy z krotki słownik
    dict(
        # sortujemy tablicę krotek
        sorted(
            # korzystamy z licznika i wyciągamy z niego krotki (długość, ilość)
            Counter(
                # dla każdego słowa w tablicy wykonujemy funkcję
                map(
                    # funkcja licząca długość podanego stringa
                    lambda x: len(x),
                    # wczytujemy dane z konsoli i rodzielamy je na słowa
                    sys.stdin.read().split()
                )
            ).items()
        )
    )
)

'''
# oneliner:
import sys; from collections import Counter; print(dict(sorted(Counter(map(lambda x: len(x), sys.stdin.read().split())).items())))
'''
