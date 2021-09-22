from operacje import Operacje
import unittest, sys, os

class Test_Operacje(unittest.TestCase):

    def test_suma_3arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2, 3), 4)

    def test_suma_2arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1, 2), 5)

    def test_suma_1arg(self):
        op = Operacje()
        self.assertEqual(op.suma(1), None)

    def test_suma_0arg(self):
        op = Operacje()
        with self.assertRaises(TypeError):
            op.suma()
    

    def test_roznica_2arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(2, 1), 4)

    def test_roznica_1arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(2), 5)

    def test_roznica_0arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(), 6)


    def test_zmiana_suma(self):
        op = Operacje()
        op['suma'] = [1, 2]
        self.assertEqual(op.argumentySuma, [1, 2])

    def test_zmiana_roznica(self):
        op = Operacje()
        op['roznica'] = [1, 2, 3]
        self.assertEqual(op.argumentyRoznica, [1, 2, 3])
    
    
    def test_po_zmianie_suma_2arg(self):
        op = Operacje()
        op['suma'] = [1, 2]
        self.assertEqual(op.suma(1, 2), 2)

    def test_po_zmianie_roznica_1arg(self):
        op = Operacje()
        op['roznica'] = [1, 2, 3]
        self.assertEqual(op.roznica(2), 2)


if __name__ == '__main__':
    sys.stdout = open(os.devnull, 'w')
    unittest.main()

