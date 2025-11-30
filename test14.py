import unittest

from plik14 import pomnoz


# Klasa z testami
class TestPomnoz(unittest.TestCase):
    def test_liczb_dodatnich(self):
        self.assertEqual(pomnoz(4,5), 20)
        self.assertEqual(pomnoz(11,11), 121)
    def test_przez_zero(self):
        self.assertEqual(pomnoz(5,0), 0)
    def test_liczby_ujemne(self):
        self.assertEqual(pomnoz(-5,-6), 30)
    def test_liczby_mieszane(self):
        self.assertEqual(pomnoz(-5,2), -10)

if __name__ == '__main__':
    unittest.main()