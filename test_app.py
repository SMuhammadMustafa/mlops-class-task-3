# test_app.py
import unittest
from app import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 4), 7)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -1), -2)
    
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)
        
if __name__ == '__main__':
    unittest.main()
