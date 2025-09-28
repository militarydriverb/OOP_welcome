import pytest

from src.models import Category, Product
from tests.conftest import first_category, second_category, first_product, second_product, third_product, fourth_product


def test_category_init(first_category, second_category):
    """Тест инициализации категории."""
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только "
                                          "коммуникации, но и получения "
                                          "дополнительных функций "
                                          "для удобства жизни")
    assert first_category.products_in_list == ['product1', 'product2', 'product3']
    assert len(first_category.products_in_list) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который "
                                           "позволяет наслаждаться просмотром,"
                                           " станет вашим другом и помощником")
    assert second_category.products_in_list == ['product4']
    assert len(second_category.products_in_list) == 1


def test_category_products_property(first_category, second_category):
    """Тест метода products — форматирование списка продуктов в виде строки."""
    assert (first_category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                       "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                       "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")


def test_add_product(first_category, first_product):
    assert len(first_category.products_in_list) == 3
    first_category.add_product = first_product  #= Добавляем продукт в список
    assert len(first_category.products_in_list) == 4


def test_product_init(first_product, second_product):
    """Тест инициализации продукта."""
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_products_str(first_product):
        assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_total_price(product_with_total_price1, product_with_total_price2):
    assert product_with_total_price1 + product_with_total_price2 == 2580000


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, Количество продуктов: 27 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)

