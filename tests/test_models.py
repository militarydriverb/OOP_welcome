from unittest.mock import Mock

import pytest

from src.models import Category, Product
from tests.conftest import first_category, first_product, second_product


def test_category_init(first_category, second_category):
    """Тест инициализации категории."""
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только "
        "коммуникации, но и получения "
        "дополнительных функций "
        "для удобства жизни"
    )
    assert first_category.products_in_list == ["product1", "product2", "product3"]
    assert len(first_category.products_in_list) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == (
        "Современный телевизор, который "
        "позволяет наслаждаться просмотром,"
        " станет вашим другом и помощником"
    )
    assert second_category.products_in_list == ["product4"]
    assert len(second_category.products_in_list) == 1


def test_category_products_property(first_category):
    """Тест метода products — форматирование списка продуктов в виде строки."""
    assert first_category.products_in_list == ["product1", "product2", "product3"]



def test_add_product(first_category, first_product):
    assert len(first_category.products_in_list) == 3
    first_category.add_product(first_product)  #= Добавляем продукт в список
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


def test_smartphone_init(test_smartphone1, test_smartphone2):
    """Тест инициализации продукта (смартфон1)."""
    assert test_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone1.price == 180000.0
    assert test_smartphone1.quantity == 5
    assert test_smartphone1.efficiency == 95.5
    assert test_smartphone1.model == "S23 Ultra"
    assert test_smartphone1.memory == 256
    assert test_smartphone1.color == "Серый"

    assert test_smartphone2.name == "Iphone 15"
    assert test_smartphone2.description == "512GB, Gray space"
    assert test_smartphone2.price == 210000.0
    assert test_smartphone2.quantity == 8
    assert test_smartphone2.efficiency == 98.2
    assert test_smartphone2.model == "15"
    assert test_smartphone2.memory == 512
    assert test_smartphone2.color == "Gray space"


def test_grass_init(test_grass1, test_grass2):
    assert test_grass1.name == "Газонная трава"
    assert test_grass1.description == "Элитная трава для газона"
    assert test_grass1.price == 500.0
    assert test_grass1.quantity == 20
    assert test_grass1.country == "Россия"
    assert test_grass1.germination_period == "7 дней"
    assert test_grass1.color == "Зеленый"

    assert test_grass2.name == "Газонная трава 2"
    assert test_grass2.description == "Выносливая трава"
    assert test_grass2.price == 450.0
    assert test_grass2.quantity == 15
    assert test_grass2.country == "США"
    assert test_grass2.germination_period == "5 дней"
    assert test_grass2.color == "Темно-зеленый"


def test_smartphone_summary(test_smartphone1, test_smartphone2):
    assert test_smartphone1 + test_smartphone2 == 2580000.0


def test_smartphone_summary_error(test_smartphone1, test_smartphone2):
    with pytest.raises(TypeError):
        assert test_smartphone1 + 1
        assert test_smartphone2 + 1


def test_grass_summary(test_grass1, test_grass2):
    assert test_grass1 + test_grass2 == 16750.0


def test_grass_summary_error(test_grass1, test_grass2):
    with pytest.raises(TypeError):
        assert test_grass1 + 1
        assert test_grass2 + 1

class TestNewProduct:
    def test_new_product_not_in_existing(self):
        product_dict = {
            "name": "Samsung Galaxy S23",
            "price": 180000.0,
            "quantity": 5,
            "description": "Описание"
        }
        existing_products = []

        new_product = Product.new_product(product_dict, existing_products)

        assert new_product.name == "Samsung Galaxy S23"
        assert new_product.price == 180000.0
        assert new_product.quantity == 5
        assert new_product.description == "Описание"


    def test_existing_product_price_not_changed(self):
        existing_product = Mock()
        existing_product.name = "Samsung Galaxy S23"
        existing_product.price = 190000.0
        existing_product.quantity = 3
        existing_products = [existing_product]

        product_dict = {
            "name": "Samsung Galaxy S23",
            "price": 180000.0,
            "quantity": 5,
            "description": "Описание"
        }

        new_product = Product.new_product(product_dict, existing_products)

        assert new_product is existing_product
        assert new_product.quantity == 8
        assert new_product.price == 190000.0  # старая цена выше

    def test_quantity_is_zero_does_not_add(self):
        existing_product = Mock()
        existing_product.name = "Samsung Galaxy S23"
        existing_product.price = 180000.0
        existing_product.quantity = 3
        existing_products = [existing_product]

        product_dict = {
            "name": "Samsung Galaxy S23",
            "price": 180000.0,
            "quantity": 0,
            "description": "Описание"
        }

        new_product = Product.new_product(product_dict, existing_products)

        assert new_product is existing_product
        assert new_product.quantity == 3  # 0 не добавлено

    def test_missing_quantity_defaults_to_zero(self):
        existing_product = Mock()
        existing_product.name = "Samsung Galaxy S23"
        existing_product.price = 180000.0
        existing_product.quantity = 3
        existing_products = [existing_product]

        product_dict = {
            "name": "Samsung Galaxy S23",
            "price": 180000.0,
            "description": "Описание"
        }

        new_product = Product.new_product(product_dict, existing_products)

        assert new_product is existing_product
        assert new_product.quantity == 3  # quantity не изменился

    def test_missing_price_defaults_to_zero(self):
        existing_product = Mock()
        existing_product.name = "Samsung Galaxy S23"
        existing_product.price = 180000.0
        existing_product.quantity = 3
        existing_products = [existing_product]

        product_dict = {
            "name": "Samsung Galaxy S23",
            "quantity": 5,
            "description": "Описание"
        }

        new_product = Product.new_product(product_dict, existing_products)

        assert new_product is existing_product
        assert new_product.quantity == 8
        assert new_product.price == 180000.0  # price не изменился