import unittest, os

class Example(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(1+1, 2, "SUM unittest failed")

    def test_subtract(self):
        self.assertEqual(2-1, 1, "SUBTRACT unittest failed")

    def test_multiply(self):
        self.assertEqual(1*2, 2, "MULTIPLY unittest failed")

    def test_division(self):
        self.assertEqual(2/2, 1, "DIVISION unittest failed")
