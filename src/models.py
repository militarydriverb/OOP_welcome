class Product:
    """Класс продукта"""

    def __init__(self, name: str, description: str, price: float,
                 quantity: int, total_price: float = 0):
        """
        Метод для инициализации (конструктор) экземпляра класса.
        Задаем значения атрибутам экземплярам.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self):
        """
        Переопределение метода__str__, который возвращает строку в формате:
        Название продукта, X руб. Остаток: X шт.
        """
        return (
            f"{self.name}, "
            f"{self.__price} руб., "
            f"Остаток: {self.quantity} шт."
        )

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
            confirmation = input(
                f"Вы хотите понизить цену {self.name} с {self.__price} "
                f"до {new_price}? (y/n): ").strip().lower()
            if confirmation != 'y':
                print("Изменение цены отменено.")
                return

        self.__price = new_price


class ProductIterator:
    """
    Класс итератор для итерации по списку продуктов
    """
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            result = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


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

    def __str__(self):
        """
        Метод для получения информации о категории
        продуктов в виде строки Название категории, название продукта, цена, продуктов и
        их количества, а также подсчитывается общее количество продуктов товаров на складе."""
        quantity_sum = 0
        for product in self.__products:
            if product.quantity > 0:
                quantity_sum += product.quantity
            else:
                self.__products.remove(product)
        if self.__products:
            return (
                f"{self.name}, "
                f"Количество продуктов: {quantity_sum} шт."
            )
        else:
            return None

    def add_product(self, product: Product):
        """Метод для создания экземпляра класса на основе словаря"""
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        """ Метод для получения списка продуктов
        и их вывода в виде строки"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
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

    print(str(product1)) # pragma: no cover
    print(str(product2)) # pragma: no cover
    print(str(product3)) # pragma: no cover

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )  # pragma: no cover

print() # pragma: no cover
print(str(category1))  # pragma: no cover
print() # pragma: no cover
print(category1.products)  # pragma: no cover

print(product1 + product2)  # pragma: no cover
print(product1 + product3)  # pragma: no cover
print(product2 + product3)  # pragma: no cover
print() # pragma: no cover

iterator = ProductIterator(category1)  # pragma: no cover
for product in iterator:  # pragma: no cover
    print(product)
    print()# pragma: no cover

