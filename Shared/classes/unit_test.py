import unittest
from BLL.classes.calculator import Calculator


class UnitTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator(17, 8, "+").result, 25)
        self.assertEqual(Calculator(-17, 8, "+").result, -9)

    def test_subtraction(self):
        self.assertEqual(Calculator(17, 8, "-").result, 9)
        self.assertEqual(Calculator(8, 17, "-").result, -9)

    def test_multiplication(self):
        self.assertEqual(Calculator(20, 0.2, "*").result, 4)
        self.assertEqual(Calculator(5, -4, "*").result, -20)
        self.assertEqual(Calculator(5, 0, "*").result, 0)

    def test_division(self):
        self.assertEqual(Calculator(10, 0.5, "/").result, 20)
        self.assertEqual(Calculator(10, -2, "/").result, -5)
        self.assertEqual(Calculator(10, 4, "/", 1).result, 2.5)
        with self.assertRaises(ZeroDivisionError):
            Calculator(10, 0, "/")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            Calculator(10, 0, "&")
