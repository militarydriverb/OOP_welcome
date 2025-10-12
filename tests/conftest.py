import pytest

from src.models import Category
from src.models import Product
from src.models import Smartphone
from src.models import LawnGrass

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
def first1_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
         ]
     )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться "
                    "просмотром, станет вашим другом и помощником",
        products=['product4']
        )



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

@pytest.fixture
def test_smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

@pytest.fixture
def test_smartphone2():
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )

@pytest.fixture
def test_grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

@pytest.fixture
def test_grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

@pytest.fixture
def category_with_no_products():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[]
        )
