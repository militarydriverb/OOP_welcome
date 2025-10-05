from src.models import Product
from src.models import Smartphone
from src.models import LawnGrass

def test_print_mixin(capsys):
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", price = 180000.0, quantity = 5)
    print(product)

    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    smartphone=Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    print(smartphone)

    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    lawn_grass = LawnGrass(
            "Газонная трава",
            "Элитная трава для газона",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый",
        )
    print(lawn_grass)

    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
