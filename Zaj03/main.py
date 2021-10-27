from klasa import Klasa

obiekt1 = Klasa(['a', 'b', 'c'])
obiekt2 = Klasa(['x', 'y', 'z'])
print('*' * 30)
print("Po utworzeniu obiektów")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
Klasa.tab = [4, 5, 6]
print("Po wykonaniu instrukcji '\u001b[31mKlasa.tab = [4, 5, 6]\u001b[0m'")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print("Po wykonaniu instrukcji '\u001b[31mobiekt1.tab = [7, 8, 9]\u001b[0m'")
obiekt1.tab = [7, 8, 9]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print("Po wykonaniu instrukcji '\u001b[31mobiekt2.tab = [-3, -2, -1]\u001b[0m'")
obiekt2.tab = [-3, -2, -1]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('*' * 30)