from DeanerySystem.day import Day
from DeanerySystem.term import Term

term1 = Term(Day.TUE, 9, 45)
print(term1)                     # Ma się wypisać: "Wtorek 9:45 [90]"
term2 = Term(Day.WED, 10, 15)
print(term2)                     # Ma się wypisać: "Środa 10:15 [90]"
print(term1.earlierThan(term2)); # Ma się wypisać: "True"
print(term1.laterThan(term2));   # Ma się wypisać: "False"
print(term1.equals(term2));      # Ma się wypisać: "False"