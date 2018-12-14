import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    
    
    def setUp(self):
        self.calc = Calculator()
    

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    

    """def test_string_numbers(self):
        self.assertEqual(self.calc.add("two", "three"), "Five")
    """

    def test_typeerror_raised(self):
        self.assertRaises(TypeError, self.calc.add, "Invalid Values")


if __name__ == "__main__":
    unittest.main()
        

