"""Повышенное задание №3: система заказов (классы «Товар», «Корзина», «Заказ»).

Деньги хранятся в Decimal, чтобы 0.1 + 0.2 давало ровно 0.30.
"""

from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def to_money(value):
    """Привести число или строку к Decimal с двумя знаками после запятой."""
    return Decimal(str(value)).quantize(CENTS, rounding=ROUND_HALF_UP)


class Product:
    """Товар. Два товара с одинаковым артикулом считаются одним товаром."""

    def __init__(self, sku, name, price):
        price = to_money(price)
        if price <= 0:
            raise ValueError("Цена товара должна быть положительной")
        self.sku = sku
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku

    def __hash__(self):
        return hash(self.sku)

    def __repr__(self):
        return f"Product({self.sku!r}, {self.name!r}, {self.price})"


class Cart:
    """Корзина: товар -> количество."""

    def __init__(self):
        self._items = {}

    def add(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self._items[product] = self._items.get(product, 0) + quantity

    def remove(self, product, quantity=None):
        """Убрать товар целиком или уменьшить его количество."""
        if product not in self._items:
            raise KeyError(f"Товара {product.name!r} нет в корзине")
        if quantity is None or quantity >= self._items[product]:
            del self._items[product]
        else:
            self._items[product] -= quantity

    def quantity(self, product):
        return self._items.get(product, 0)

    def total(self):
        return sum((product.price * count
                    for product, count in self._items.items()),
                   Decimal("0.00"))

    def items(self):
        """Список пар (товар, количество)."""
        return list(self._items.items())

    def clear(self):
        self._items.clear()

    def is_empty(self):
        return not self._items

    def __len__(self):
        """Общее количество единиц товара в корзине."""
        return sum(self._items.values())


class Order:
    """Заказ, оформленный из корзины.

    Статусы: new -> paid -> shipped; отменить можно только неоплаченный.
    """

    _next_id = 1

    def __init__(self, cart, customer):
        if cart.is_empty():
            raise ValueError("Нельзя оформить заказ из пустой корзины")
        self.order_id = Order._next_id
        Order._next_id += 1
        self.customer = customer
        self.lines = cart.items()
        self.total = cart.total()
        self.status = "new"
        cart.clear()

    def pay(self):
        self._change_status("new", "paid")

    def ship(self):
        self._change_status("paid", "shipped")

    def cancel(self):
        self._change_status("new", "cancelled")

    def _change_status(self, expected, new_status):
        if self.status != expected:
            raise RuntimeError(
                f"Заказ №{self.order_id} в статусе {self.status!r}, "
                f"переход в {new_status!r} невозможен"
            )
        self.status = new_status

    def receipt(self):
        """Текст чека по заказу."""
        lines = [f"Заказ №{self.order_id}, покупатель: {self.customer}"]
        for product, count in self.lines:
            cost = product.price * count
            lines.append(f"  {product.name} x{count} = {cost} руб.")
        lines.append(f"Итого: {self.total} руб.")
        return "\n".join(lines)
