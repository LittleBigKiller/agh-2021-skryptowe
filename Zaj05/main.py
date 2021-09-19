from DeanerySystem import *

term1 = Term(8, 0, Day.WED)
term2 = Term(9, 30, Day.WED)
term3 = Term(9, 35, Day.THU)

bl = [Break(Term(9, 30, Day.MON, 5))]

tt2 = Timetable2(bl)

l1 = Lesson(tt2, term1, 'lesson1', 'lesson1', 2)
l2 = Lesson(tt2, term2, 'lesson2', 'lesson2', 2)
l3 = Lesson(tt2, term3, 'lesson3', 'lesson3', 2)

print(tt2)

tt2.put(l1)

print(tt2)

tt2.put(l2)

print(tt2)

tt2.put(l3)

print(tt2)

#l1.laterTime()
#l3.earlierTime()

print(tt2)
