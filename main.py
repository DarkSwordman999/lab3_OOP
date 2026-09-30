"""Лабораторная работа №3, вариант 10: демонстрация всех классов."""

from counter import Counter
from float_range import FloatRange
from shop import Cart, Order, Product
from student import Student


def demo_student():
    print("=== Студент ===")
    student = Student("Фураев Владислав Викторович", "221341", [5, 4])
    student.add_grade(5)
    student.print_info()


def demo_counter():
    print("\n=== Счётчик ===")
    counter = Counter(start=0, step=2, minimum=0, maximum=6)
    print("Увеличиваем:", counter.increment(), counter.increment())
    print("Уменьшаем:", counter.decrement())
    try:
        counter.increment(5)
    except ValueError as error:
        print("Ошибка:", error)
    print(counter)


def demo_iterator():
    print("\n=== Итератор FloatRange ===")
    print("От 0 до 1 с шагом 0.2:", list(FloatRange(0, 1, 0.2)))
    for value in FloatRange(1.5, 0, -0.5):
        print("  значение", value)


def demo_shop():
    print("\n=== Система заказов ===")
    pen = Product("P-1", "Ручка гелевая", "25.50")
    notebook = Product("N-1", "Тетрадь 48 листов", 59.9)
    cart = Cart()
    cart.add(pen, 3)
    cart.add(notebook)
    cart.remove(pen, 1)
    print(f"В корзине {len(cart)} шт. на сумму {cart.total()} руб.")

    order = Order(cart, "Фураев В. В.")
    print(order.receipt())
    order.pay()
    order.ship()
    print("Статус заказа:", order.status)
    print("Корзина пуста:", cart.is_empty())


def main():
    demo_student()
    demo_counter()
    demo_iterator()
    demo_shop()


if __name__ == "__main__":
    main()
