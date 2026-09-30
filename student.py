"""Задание средней сложности №2: класс «Студент» с выводом информации."""


class Student:
    """Студент с ФИО, группой и списком оценок."""

    MIN_GRADE = 2
    MAX_GRADE = 5

    def __init__(self, full_name, group, grades=None):
        if not full_name or not full_name.strip():
            raise ValueError("ФИО студента не может быть пустым")
        self.full_name = full_name.strip()
        self.group = group
        self._grades = []
        for grade in grades or []:
            self.add_grade(grade)

    @property
    def grades(self):
        """Оценки только для чтения (копия в виде кортежа)."""
        return tuple(self._grades)

    def add_grade(self, grade):
        if not isinstance(grade, int) or isinstance(grade, bool):
            raise TypeError("Оценка должна быть целым числом")
        if not self.MIN_GRADE <= grade <= self.MAX_GRADE:
            raise ValueError(
                f"Оценка должна быть от {self.MIN_GRADE} до {self.MAX_GRADE}"
            )
        self._grades.append(grade)

    def average(self):
        """Средний балл, округлённый до сотых; 0.0, если оценок нет."""
        if not self._grades:
            return 0.0
        return round(sum(self._grades) / len(self._grades), 2)

    def info(self):
        """Вернуть информацию о студенте в виде многострочного текста."""
        grades = ", ".join(map(str, self._grades)) or "нет"
        return (
            f"Студент: {self.full_name}\n"
            f"Группа: {self.group}\n"
            f"Оценки: {grades}\n"
            f"Средний балл: {self.average():.2f}"
        )

    def print_info(self):
        """Вывести информацию о студенте на экран."""
        print(self.info())

    def __str__(self):
        return f"{self.full_name} ({self.group})"

    def __repr__(self):
        return (f"Student({self.full_name!r}, {self.group!r}, "
                f"{list(self._grades)!r})")
