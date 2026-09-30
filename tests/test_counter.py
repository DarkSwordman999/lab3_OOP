import unittest

from counter import Counter


class CounterTest(unittest.TestCase):
    def test_default_counter(self):
        counter = Counter()
        self.assertEqual(counter.value, 0)
        self.assertEqual(counter.increment(), 1)
        self.assertEqual(counter.increment(), 2)
        self.assertEqual(counter.decrement(), 1)

    def test_step_and_times(self):
        counter = Counter(start=10, step=5)
        self.assertEqual(counter.increment(3), 25)
        self.assertEqual(counter.decrement(), 20)

    def test_bounds(self):
        counter = Counter(start=0, minimum=0, maximum=2)
        counter.increment(2)
        with self.assertRaises(ValueError):
            counter.increment()
        self.assertEqual(counter.value, 2)  # значение не испортилось
        counter.reset()
        with self.assertRaises(ValueError):
            counter.decrement()

    def test_invalid_settings(self):
        with self.assertRaises(ValueError):
            Counter(step=0)
        with self.assertRaises(ValueError):
            Counter(minimum=5, maximum=1)
        with self.assertRaises(ValueError):
            Counter(start=-1, minimum=0)

    def test_value_is_read_only(self):
        with self.assertRaises(AttributeError):
            Counter().value = 100

    def test_reset_and_int(self):
        counter = Counter(start=7)
        counter.increment(4)
        counter.reset()
        self.assertEqual(int(counter), 7)


if __name__ == "__main__":
    unittest.main()
