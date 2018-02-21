import unittest, os

class Example(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(1+1, 3, "SUM unittest failed")

    def test_subtract(self):
        self.assertEqual(2-1, 3, "SUBTRACT unnittest failed")

    def test_multiply(self):
        self.assertEqual(1*2, 3, "MULTIPLY unnittest failed")

    def test_division(self):
        self.assertEqual(2/2, 3, "DIVISION unittest failed")