import unittest
from remainder import compute_remainder

class TestComputeRemainder(unittest.TestCase):
    def test_positive_dividend_positive_divisor(self):
        self.assertEqual(compute_remainder(10, 3), 1, "10 % 3 должно быть 1")

    def test_negative_dividend_positive_divisor(self):
        self.assertEqual(compute_remainder(-10, 3), 2, "-10 % 3 должно быть 2")

    def test_positive_dividend_negative_divisor(self):
        self.assertEqual(compute_remainder(10, -3), -2, "10 % -3 должно быть -2")

    def test_negative_dividend_negative_divisor(self):
        self.assertEqual(compute_remainder(-10, -3), -1, "-10 % -3 должно быть -1")

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            compute_remainder(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль невозможно.", "Ожидается исключение при делении на ноль")

if __name__ == '__main__':
    unittest.main()
