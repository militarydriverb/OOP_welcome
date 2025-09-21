import pytest

from src.models import Category
from src.models import Product

"""Создаем фикстуры для тестов"""


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=['product1', 'product2', 'product3']
    )
    #         Product("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"),
    #         Product("Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"),
    #         Product("Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"),
    #     ]
    # )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться "
                    "просмотром, станет вашим другом и помощником",
        products=['product4']
        )
    #         Product("55\" QLED 4K, Фоновая подсветка,123000.0 руб. Остаток: 7 шт.\n"),
    #     ]
    # )


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def third_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def fourth_product():
    return Product(
        name="LG 55UM7500",
        description="55UM7500, 4K, 55'",
        price=110000.0,
        quantity=10
    )
