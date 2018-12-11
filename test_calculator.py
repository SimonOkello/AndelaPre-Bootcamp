import unittest
from calculator import Calculator

class TestCalc(unittest.TestCase):
    def testAdd(self):
        calc = Calculator()
        result = calc.add(3, 6)
        self.assertEqual(result, 9)
        
if __name__ == "__main__":
    unittest.main()