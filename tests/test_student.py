import io
import unittest
from contextlib import redirect_stdout

from student import Student


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student("Иванов Иван Иванович", "221341", [5, 4, 5])

    def test_fields(self):
        self.assertEqual(self.student.full_name, "Иванов Иван Иванович")
        self.assertEqual(self.student.group, "221341")
        self.assertEqual(self.student.grades, (5, 4, 5))

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            Student("   ", "221341")

    def test_add_grade_and_average(self):
        self.student.add_grade(3)
        self.assertEqual(self.student.average(), 4.25)

    def test_average_without_grades(self):
        self.assertEqual(Student("Петров П. П.", "221341").average(), 0.0)

    def test_wrong_grades(self):
        with self.assertRaises(ValueError):
            self.student.add_grade(6)
        with self.assertRaises(TypeError):
            self.student.add_grade("5")
        with self.assertRaises(TypeError):
            self.student.add_grade(True)

    def test_grades_cannot_be_changed_from_outside(self):
        with self.assertRaises(AttributeError):
            self.student.grades.append(2)

    def test_info(self):
        self.assertEqual(
            self.student.info(),
            "Студент: Иванов Иван Иванович\n"
            "Группа: 221341\n"
            "Оценки: 5, 4, 5\n"
            "Средний балл: 4.67",
        )

    def test_print_info(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.student.print_info()
        self.assertIn("Средний балл: 4.67", buffer.getvalue())

    def test_str(self):
        self.assertEqual(str(self.student), "Иванов Иван Иванович (221341)")


if __name__ == "__main__":
    unittest.main()
