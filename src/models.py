class Product:
    """Класс продукта"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int):
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
            confirmation = input(
                f"Вы хотите понизить цену {self.name} с {self.__price} "
                f"до {new_price}? (y/n): ").strip().lower()
            if confirmation != 'y':
                print("Изменение цены отменено.")
                return

        self.__price = new_price


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
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        """ Метод для получения списка продуктов"""
        products_str = ""
        for product in self.__products:
            products_str += (f"{product.name}, {product.price} руб. "
                             f"Остаток: {product.quantity} шт.\n")
        return products_str

    # @products.setter
    # def products(self, product: Product):
    #     """Метод для создания экземпляра класса на основе словаря"""
    #     if product not in self.__products:
    #         self.__products.append(product)
    #         Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)  # pragma: no cover
    product2 = Product("Iphone 15", "512GB, Gray space",
                       210000.0, 8)  # pragma: no cover
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий",
                       31000.0, 14)  # pragma: no cover

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )  # pragma: no cover
    product_list = [product1, product2, product3,] # pragma: no cover

    print(category1.products)# pragma: no cover
    print(Category.category_count)  # pragma: no cover
    print(category1.product_count) # pragma: no cover

    product4 = Product("55\" QLED 4K", "Фоновая подсветка",
                       123000.0, 7)  # pragma: no cover
    category1.add_product(product4)  # pragma: no cover
    print(category1.products) # pragma: no cover
    print(Category.category_count)  # pragma: no cover
    print(category1.product_count) # pragma: no cover

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra",
         "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0, "quantity": 5}, product_list)  # pragma: no cover
    print(new_product.name)  # pragma: no cover
    print(new_product.description)  # pragma: no cover
    print(new_product.price)  # pragma: no cover
    print(new_product.quantity)  # pragma: no cover

    new_product.price = 800  # pragma: no cover
    print(new_product.price)  # pragma: no cover

    new_product.price = -100  # pragma: no cover
    print(new_product.price)  # pragma: no cover
    new_product.price = 0  # pragma: no cover
    print(new_product.price)  # pragma: no cover

    print(Category.category_count)  # pragma: no cover
    print(Category.product_count)  # pragma: no cover
