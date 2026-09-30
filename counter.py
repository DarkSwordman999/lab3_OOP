"""Задание средней сложности №8: класс-счётчик (увеличение/уменьшение)."""


class Counter:
    """Счётчик с шагом и необязательными нижней и верхней границами.

    Значение меняется только методами, выход за границы запрещён.
    """

    def __init__(self, start=0, step=1, minimum=None, maximum=None):
        if step <= 0:
            raise ValueError("Шаг счётчика должен быть положительным")
        if minimum is not None and maximum is not None and minimum > maximum:
            raise ValueError("Нижняя граница больше верхней")
        self._start = start
        self._step = step
        self.minimum = minimum
        self.maximum = maximum
        self._check(start)
        self._value = start

    @property
    def value(self):
        return self._value

    def _check(self, value):
        if self.minimum is not None and value < self.minimum:
            raise ValueError(
                f"Значение {value} меньше минимума {self.minimum}"
            )
        if self.maximum is not None and value > self.maximum:
            raise ValueError(
                f"Значение {value} больше максимума {self.maximum}"
            )

    def increment(self, times=1):
        new_value = self._value + self._step * times
        self._check(new_value)
        self._value = new_value
        return self._value

    def decrement(self, times=1):
        new_value = self._value - self._step * times
        self._check(new_value)
        self._value = new_value
        return self._value

    def reset(self):
        self._value = self._start

    def __int__(self):
        return self._value

    def __repr__(self):
        return f"Counter(value={self._value}, step={self._step})"
