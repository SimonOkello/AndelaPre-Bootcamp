import unittest
class Calculate(object):
 def add(self, x, y):
     return x + y

class TestCalc(unittest.TestCase):
    def testAdd(self):
        calc = Calculate()
        result = calc.add(2, 2)
        self.assertEqual(result, 4)
        print(result)

if __name__ == '__main__':
    unittest.main()


