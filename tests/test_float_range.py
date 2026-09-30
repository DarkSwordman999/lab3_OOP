import unittest

from float_range import FloatRange


class FloatRangeTest(unittest.TestCase):
    def test_fractional_step(self):
        self.assertEqual(list(FloatRange(0, 1, 0.25)),
                         [0, 0.25, 0.5, 0.75])

    def test_no_accumulated_error(self):
        values = list(FloatRange(0, 1, 0.1))
        self.assertEqual(len(values), 10)
        self.assertEqual(values[3], 0.3)

    def test_negative_step(self):
        self.assertEqual(list(FloatRange(1, 0, -0.5)), [1, 0.5])

    def test_empty(self):
        self.assertEqual(list(FloatRange(5, 1, 1)), [])

    def test_is_iterator(self):
        numbers = FloatRange(0, 3)
        self.assertIs(iter(numbers), numbers)
        self.assertEqual(next(numbers), 0)
        self.assertEqual(next(numbers), 1)
        self.assertEqual(list(numbers), [2])
        with self.assertRaises(StopIteration):
            next(numbers)

    def test_zero_step(self):
        with self.assertRaises(ValueError):
            FloatRange(0, 1, 0)


if __name__ == "__main__":
    unittest.main()
