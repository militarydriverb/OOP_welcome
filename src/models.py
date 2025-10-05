import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.base_category import BaseCategory
from src.print_mixin import PrintMixin
from src.base_product import BaseProduct


class Product(BaseProduct, PrintMixin):
    """
    Класс продукта, в который подключена цепочка наследования
    от базового класса BaseProduct и от класса PrintMixin
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        total_price: float = 0,
    ):
        """
        Метод для инициализации (конструктор) экземпляра класса.
        Задаем значения атрибутам экземплярам.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.total_price = total_price
        super().__init__()

    def __add__(self, other):
        """
         Метод для сложения двух экземпляров класса Product
        возвращает сумму произведений цены на количество у двух объектов.
        """
        if isinstance(other, Product):
            total_price = round(
                self.quantity * self.__price,
            ) + round(
                other.quantity * other.__price,
            )
            return total_price
        else:
            return NotImplemented

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list):
        """
        Метод для создания экземпляра класса на основе словаря
        При наличии товара с таким же именем:
        - складывает количество
        - выбирает максимальную цену
        """
        if existing_products:
            for product in existing_products:
                if product.name == product_dict["name"]:
                    product.quantity += product_dict.get("quantity", 0)
                    if product_dict.get("price", 0) > product.price:
                        product.price = product_dict["price"]
                    return product
        return cls(**product_dict)

    @property
    def price(self):
        """Метод для получения цены продукта"""
        if self.__price > 0:
            return self.__price
        else:
            return 0

    @price.setter
    def price(self, new_price):
        """
        Метод для установки цены продукта с проверкой
        на нулевую или отрицательную цену
        При понижении цены запрашивает подтверждение у пользователя.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return

        if new_price < self.__price:
            confirmation = (
                input(
                    f"Вы хотите понизить цену {self.name} с {self.__price} "
                    f"до {new_price}? (y/n): "
                )
                .strip()
                .lower()
            )
            if confirmation != "y":
                print("Изменение цены отменено.")
                return

        self.__price = new_price


class Smartphone(Product):
    """Класс смартфон дочерний от класса продукта"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, product: "Smartphone"):
        """функция сложения из продуктов класса Smartphone"""
        if type(product) is Smartphone:
            return Product.__add__(self, product)
        raise TypeError


class LawnGrass(Product):
    """Класс газонная трава дочерний от класса продукта"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, product: "LawnGrass"):
        """функция сложения из продуктов класса LawnGrass"""
        if type(product) is LawnGrass:
            return Product.__add__(self, product)
        raise TypeError


class Category(BaseCategory):
    """
    Класс категория продукта, в который подключена цепочка наследования
    от базового класса BaseCategory
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Метод для инициализации (конструктор) экземпляра класса.
        Задаем значения атрибутам экземпляра.
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        """Метод для создания экземпляра класса на основе словаря"""
        if isinstance(product, Product):
            """Доработка метода, который добавляет продукт в категорию,
            таким образом, чтобы не было возможности добавить вместо продукта
             или его наследников любой другой объект."""
            if product not in self.__products:
                self.__products.append(product)
                Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Метод для получения списка продуктов"""
        if issubclass(type(self), Category):
            """Защита метода так, чтобы, кроме смартфонов, травы газонной или
            других продуктов, в список нельзя было добавлять ничего другого"""
            products_str = ""
            for product in self.__products:
                products_str += (
                    f"{product.name}, {product.price} руб. "
                    f"Остаток: {product.quantity} шт.\n"
                )
            return products_str
        return None

    @property
    def products_in_list(self):
        return self.__products


if __name__ == "__main__":  # pragma: no cover
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )  # pragma: no cover
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)  # pragma: no cover
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)  # pragma: no cover

    print(product1.name)  # pragma: no cover
    print(product1.description)  # pragma: no cover
    print(product1.price)  # pragma: no cover
    print(product1.quantity)  # pragma: no cover

    print(product2.name)  # pragma: no cover
    print(product2.description)  # pragma: no cover
    print(product2.price)  # pragma: no cover
    print(product2.quantity)  # pragma: no cover

    print(product3.name)  # pragma: no cover
    print(product3.description)  # pragma: no cover
    print(product3.price)  # pragma: no cover
    print(product3.quantity)  # pragma: no cover

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )  # pragma: no cover

    print(category1.name == "Смартфоны")  # pragma: no cover
    print(category1.description)  # pragma: no cover
    print(len(category1.products_in_list))  # pragma: no cover
    print(category1.category_count)  # pragma: no cover
    print(category1.product_count)  # pragma: no cover

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)  # pragma: no cover
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product4],
    )  # pragma: no cover

    print(category2.name)  # pragma: no cover
    print(category2.description)  # pragma: no cover
    print(len(category2.products_in_list))  # pragma: no cover
    print(category2.products)  # pragma: no cover

    print(Category.category_count)  # pragma: no cover
    print(Category.product_count)  # pragma: no cover
