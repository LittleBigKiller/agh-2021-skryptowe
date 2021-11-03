import itertools

class Student():
    id_iter = itertools.count()

    def __init__(self, name, surname):
        self.__id = next(self.__class__.id_iter)
        self.name = name
        self.surname = surname

    def getId(self):
        return self.__id

    def __str__(self):
        return f'{self.name} {self.surname}'