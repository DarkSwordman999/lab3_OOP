import unittest
from decimal import Decimal

from shop import Product


class ProductTest(unittest.TestCase):
    def test_price_is_decimal(self):
        pen = Product("P-1", "Ручка", "25.5")
        self.assertEqual(pen.price, Decimal("25.50"))

    def test_price_from_float(self):
        self.assertEqual(Product("P-2", "Тетрадь", 0.1).price,
                         Decimal("0.10"))

    def test_non_positive_price(self):
        with self.assertRaises(ValueError):
            Product("P-3", "Ластик", 0)
        with self.assertRaises(ValueError):
            Product("P-3", "Ластик", -10)

    def test_equality_by_sku(self):
        self.assertEqual(Product("A", "Ручка", 10), Product("A", "Pen", 12))
        self.assertNotEqual(Product("A", "Ручка", 10),
                            Product("B", "Ручка", 10))
        self.assertEqual(len({Product("A", "x", 1), Product("A", "y", 2)}), 1)


if __name__ == "__main__":
    unittest.main()
