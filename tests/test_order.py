import pytest
from src.order import Order


class TestOrder:
    def test_init_valid_values(self):
        order = Order("https://example.com/product", 2, 100.0)
        assert order.link == "https://example.com/product"
        assert order.quantity == 2
        assert order.price == 100.0
        assert order.amount == 200.0


    def test_init_zero_quantity(self):
        order = Order("https://example.com/product", 0, 100.0)
        assert order.quantity == 0
        assert order.amount == 0.0


    def test_init_zero_price(self):
        order = Order("https://example.com/product", 2, 0.0)
        assert order.price == 0.0
        assert order.amount == 0.0

    def test_str_method(self):
        order = Order("https://example.com/product", 3, 50.0)
        expected = "Куплен товар https://example.com/product в количестве 3 на общую сумму 150.0."
        assert str(order) == expected

    def test_add_product_returns_string(self):
        order = Order("https://example.com/product", 2, 100.0)
        result = order.add_product()
        assert isinstance(result, str)
        assert result == str(order)

    def test_add_product_with_arguments_ignored(self):
        # Проверяем, что аргументы игнорируются
        order = Order("https://example.com/product", 2, 100.0)
        result = order.add_product("extra_arg", key="value")
        assert result == str(order)