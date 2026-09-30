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
