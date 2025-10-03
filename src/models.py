class Product:
    """Класс продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Метод для инициализации (конструктор) экземпляра класса.
        Задаем значения атрибутам экземплярам.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    def __add__(self, product: "Smartphone") -> float:
        """функция сложения из продуктов класса Smartphone"""
        if type(product) is Smartphone:
            return self.price * self.quantity + product.price * product.quantity
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

    def __add__(self, product: "LawnGrass") -> float:
        """функция сложения из продуктов класса LawnGrass"""
        if type(product) is LawnGrass:
            return self.price * self.quantity + product.price * product.quantity
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


if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )  # pragma: no cover
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )  # pragma: no cover
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )  # pragma: no cover
    print()  # pragma: no cover
    print(smartphone1.name)  # pragma: no cover
    print(smartphone1.description)  # pragma: no cover
    print(smartphone1.price)  # pragma: no cover
    print(smartphone1.quantity)  # pragma: no cover
    print(smartphone1.efficiency)  # pragma: no cover
    print(smartphone1.model)  # pragma: no cover
    print(smartphone1.memory)  # pragma: no cover
    print(smartphone1.color)  # pragma: no cover

    print()  # pragma: no cover
    print(smartphone2.name)  # pragma: no cover
    print(smartphone2.description)  # pragma: no cover
    print(smartphone2.price)  # pragma: no cover
    print(smartphone2.quantity)  # pragma: no cover
    print(smartphone2.efficiency)  # pragma: no cover
    print(smartphone2.model)  # pragma: no cover
    print(smartphone2.memory)  # pragma: no cover
    print(smartphone2.color)  # pragma: no cover

    print()  # pragma: no cover
    print(smartphone3.name)  # pragma: no cover
    print(smartphone3.description)  # pragma: no cover
    print(smartphone3.price)  # pragma: no cover
    print(smartphone3.quantity)  # pragma: no cover
    print(smartphone3.efficiency)  # pragma: no cover
    print(smartphone3.model)  # pragma: no cover
    print(smartphone3.memory)  # pragma: no cover
    print(smartphone3.color)  # pragma: no cover

    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )  # pragma: no cover
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )  # pragma: no cover
    print()  # pragma: no cover
    print(grass1.name)  # pragma: no cover
    print(grass1.description)  # pragma: no cover
    print(grass1.price)  # pragma: no cover
    print(grass1.quantity)  # pragma: no cover
    print(grass1.country)  # pragma: no cover
    print(grass1.germination_period)  # pragma: no cover
    print(grass1.color)  # pragma: no cover

    print()  # pragma: no cover
    print(grass2.name)  # pragma: no cover
    print(grass2.description)  # pragma: no cover
    print(grass2.price)  # pragma: no cover
    print(grass2.quantity)  # pragma: no cover
    print(grass2.country)  # pragma: no cover
    print(grass2.germination_period)  # pragma: no cover
    print(grass2.color)  # pragma: no cover

    print()  # pragma: no cover
    smartphone_sum = smartphone1 + smartphone2  # pragma: no cover
    print(smartphone_sum)  # pragma: no cover

    print()  # pragma: no cover
    grass_sum = grass1 + grass2  # pragma: no cover
    print(grass_sum)  # pragma: no cover

    print()  # pragma: no cover
    try:  # pragma: no cover
        invalid_sum = smartphone1 + grass1  # pragma: no cover
    except TypeError:  # pragma: no cover
        print("Возникла ошибка TypeError " "при попытке сложения")  # pragma: no cover
    else:  # pragma: no cover
        print(
            "Не возникла ошибка TypeError " "при попытке сложения"
        )  # pragma: no cover

    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )  # pragma: no cover
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )  # pragma: no cover

    category_smartphones.add_product(smartphone3)  # pragma: no cover

    print()  # pragma: no cover
    print(category_smartphones.products)  # pragma: no cover

    print()
    print(category_grass.products)  # pragma: no cover

    print()  # pragma: no cover
    print(Category.product_count)  # pragma: no cover

    try:  # pragma: no cover
        category_smartphones.add_product("Not a product")  # pragma: no cover
    except TypeError:  # pragma: no cover
        print(
            "Возникла ошибка TypeError при добавлении не продукта"
        )  # pragma: no cover
    else:  # pragma: no cover
        print(
            "Не возникла ошибка TypeError при добавлении не продукта"
        )  # pragma: no cover
