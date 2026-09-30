"""Задание средней сложности №10: класс-итератор."""


class FloatRange:
    """Аналог range, который умеет работать с дробным шагом.

    Объект сам является итератором (__iter__ возвращает self), поэтому
    пройти по нему можно только один раз, как по итератору из iter().
    Очередное значение считается как start + index * step, а не
    накоплением суммы, чтобы не копить ошибку округления.
    """

    def __init__(self, start, stop, step=1.0):
        if step == 0:
            raise ValueError("Шаг не может быть равен нулю")
        self.start = start
        self.stop = stop
        self.step = step
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = round(self.start + self._index * self.step, 10)
        if self.step > 0 and value >= self.stop:
            raise StopIteration
        if self.step < 0 and value <= self.stop:
            raise StopIteration
        self._index += 1
        return value
