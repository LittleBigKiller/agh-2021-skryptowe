import ksiazki
import unittest

class Test_Ksiazki(unittest.TestCase):
    def test_params_simple_insert(self):
        self.assertEqual(ksiazki.process_params(['a:1']), {'a':1})

    def test_params_complex_insert(self):
        self.assertEqual(ksiazki.process_params(['a:1', 'b:3', 'd:2']), {'a':1, 'b':3, 'd':2})

    def test_params_no_colon_insert(self):
        self.assertEqual(ksiazki.process_params(['a:1', 'basd']), {'a':1})

    def test_params_multi_colon_insert(self):
        self.assertEqual(ksiazki.process_params(['a:1', 'bas:1:fgs']), {'a':1})

    def test_params_non_number_insert(self):
        self.assertEqual(ksiazki.process_params(['a:1', 'b:g']), {'a':1})


    def test_input_simple_borrow(self):
        bd = {'a':1, 'b':2}
        self.assertEqual(ksiazki.process_input([['imie', 'a', 'pozycz']], bd), ({'imie': ['a']}, {'a':0, 'b':2}))

    def test_input_complex_borrow(self):
        bd = {'a':1, 'b':2}
        actions = [['imie', 'a', 'pozycz'], ['imie', 'b', 'pozycz'], ['imie', 'a', 'pozycz'], ['imie', 'b', 'pozycz']]
        self.assertEqual(ksiazki.process_input(actions, bd), ({'imie': ['a', 'b', 'b']}, {'a':0, 'b':0}))

    def test_input_simple_return(self):
        bd = {'a':1, 'b':2}
        self.assertEqual(ksiazki.process_input([['imie', 'a', 'pozycz'], ['imie', 'a', 'zwroc']], bd), ({'imie': []}, {'a':1, 'b':2}))

    def test_input_complex_return(self):
        bd = {'a':1, 'b':2}
        actions = [['imie', 'a', 'pozycz'], ['imie', 'b', 'pozycz'], ['imie', 'a', 'zwroc'], ['imie', 'b', 'pozycz'], ['imie', 'a', 'pozycz'], ['imie', 'b', 'zwroc']]
        self.assertEqual(ksiazki.process_input(actions, bd), ({'imie': ['b', 'a']}, {'a':0, 'b':1}))

    def test_input_invalid_action(self):
        bd = {'a':1, 'b':2}
        self.assertEqual(ksiazki.process_input([['imie', 'a', 'test']], bd), ({}, {'a':1, 'b':2}))

    def test_input_invalid_book_borrow(self):
        bd = {'a':1, 'b':2}
        self.assertEqual(ksiazki.process_input([['imie', 'c', 'pozycz']], bd), ({}, {'a':1, 'b':2}))

    def test_input_invalid_book_return(self):
        bd = {'a':1, 'b':2}
        self.assertEqual(ksiazki.process_input([['imie', 'c', 'zwroc']], bd), ({}, {'a':1, 'b':2}))


if __name__ == '__main__':
    unittest.main()
