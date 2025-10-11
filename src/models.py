class Product:
    """Класс продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int, total_price: float = 0):
        """
        Метод для инициализации (конструктор) экземпляра класса.
        Задаем значения атрибутам экземплярам.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.total_price = total_price

    def __add__(self, other):
        """
         Метод для сложения двух экземпляров класса Product
        возвращает сумму произведений цены на количество у двух объектов.
        """
        if isinstance(other, Product):
            total_price = (round(self.quantity * self.__price,) +
                    round(other.quantity * other.__price,))
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


class Category:
    """Класс категория продукта"""

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


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
