import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def testAdd(self):

              result = self.calc.add(4, 7)
              self.assertEqual(result, 11)
    if __name__ == "main":
        unittest.main()