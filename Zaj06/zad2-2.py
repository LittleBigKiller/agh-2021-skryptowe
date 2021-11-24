'''
import sys
from collections import Counter

# wczytaj dane z stdin
sys.stdin.read()

# rozbij na listę pojedynczych słów
sys.stdin.read().split()

# dla x podaj jego długość (jeśli string/lista)
lambda x: len(x)

# na każdym elemencie listy słów wykonaj powyższą funkcję
map(lambda x: len(x), sys.stdin.read().split())

# policz ile jest elementów o jakiej wartości
Counter(map(lambda x: len(x), sys.stdin.read().split()))

# zamień obiekt counter na siłę na słownik
dict(Counter(map(lambda x: len(x), sys.stdin.read().split())))

# gotowa funkcja:
print(dict(Counter(map(lambda x: len(x), sys.stdin.read().split()))))
'''

# oneliner:
import sys; from collections import Counter; print(dict(Counter(map(lambda x: len(x), sys.stdin.read().split()))))
