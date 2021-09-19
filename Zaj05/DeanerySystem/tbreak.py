from .term import Term

class Break:
    def __init__(self, term):
        self._term = term

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        if type(value) is not Term:
            raise TypeError('term musi być klasy \'Term\'')
        else:
            self._term = value

    def __str__(self):
        return "Przerwa"

    def getTerm(self):
        return self._term
