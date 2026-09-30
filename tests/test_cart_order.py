import unittest
from decimal import Decimal

from shop import Cart, Order, Product


class CartTest(unittest.TestCase):
    def setUp(self):
        self.pen = Product("P-1", "Ручка", "25.50")
        self.book = Product("B-1", "Тетрадь", "0.10")
        self.cart = Cart()

    def test_empty_cart(self):
        self.assertTrue(self.cart.is_empty())
        self.assertEqual(self.cart.total(), Decimal("0.00"))
        self.assertEqual(len(self.cart), 0)

    def test_add_same_product_twice(self):
        self.cart.add(self.pen)
        self.cart.add(self.pen, 2)
        self.assertEqual(self.cart.quantity(self.pen), 3)
        self.assertEqual(len(self.cart), 3)

    def test_total_is_exact(self):
        self.cart.add(self.book, 3)  # 0.10 * 3 без ошибок округления
        self.cart.add(self.pen, 2)
        self.assertEqual(self.cart.total(), Decimal("51.30"))

    def test_remove(self):
        self.cart.add(self.pen, 5)
        self.cart.remove(self.pen, 2)
        self.assertEqual(self.cart.quantity(self.pen), 3)
        self.cart.remove(self.pen)
        self.assertTrue(self.cart.is_empty())

    def test_remove_missing_product(self):
        with self.assertRaises(KeyError):
            self.cart.remove(self.pen)

    def test_wrong_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add(self.pen, 0)


class OrderTest(unittest.TestCase):
    def setUp(self):
        self.pen = Product("P-1", "Ручка", "25.50")
        self.cart = Cart()
        self.cart.add(self.pen, 2)

    def test_checkout_clears_cart(self):
        order = Order(self.cart, "Фураев В. В.")
        self.assertEqual(order.total, Decimal("51.00"))
        self.assertEqual(order.status, "new")
        self.assertTrue(self.cart.is_empty())

    def test_empty_cart_order(self):
        with self.assertRaises(ValueError):
            Order(Cart(), "Покупатель")

    def test_ids_are_unique(self):
        first = Order(self.cart, "А")
        self.cart.add(self.pen)
        second = Order(self.cart, "Б")
        self.assertEqual(second.order_id, first.order_id + 1)

    def test_status_flow(self):
        order = Order(self.cart, "Покупатель")
        order.pay()
        order.ship()
        self.assertEqual(order.status, "shipped")

    def test_invalid_transitions(self):
        order = Order(self.cart, "Покупатель")
        with self.assertRaises(RuntimeError):
            order.ship()  # нельзя отправить неоплаченный
        order.pay()
        with self.assertRaises(RuntimeError):
            order.cancel()  # нельзя отменить оплаченный

    def test_receipt(self):
        order = Order(self.cart, "Покупатель")
        text = order.receipt()
        self.assertIn("Ручка x2 = 51.00 руб.", text)
        self.assertTrue(text.endswith("Итого: 51.00 руб."))


if __name__ == "__main__":
    unittest.main()
