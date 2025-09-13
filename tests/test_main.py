from src.main import Category


def test_category_init(first_category, second_category):
    """Тест инициализации категории."""
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только "
                                          "коммуникации, но и получения "
                                          "дополнительных функций "
                                          "для удобства жизни")
    assert first_category.products == ['product1', 'product2', 'product3']
    assert len(first_category.products) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который "
                                           "позволяет наслаждаться просмотром,"
                                           " станет вашим другом и помощником")
    assert second_category.products == ['product4']
    assert len(second_category.products) == 1


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


def test_category_add_product_counter():
    """Тест подсчета количества продуктов и категорий."""
    assert Category.category_count == 2
    assert Category.product_count == 4
