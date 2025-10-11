from src.base_category import BaseCategory
from src.exceptions import ZeroOrderProductQuantity


class Order(BaseCategory):

    def __init__(self, link, quantity, price):
        self.link = link
        self.quantity = quantity
        self.price = price
        self.amount = self.quantity * self.price

    def __str__(self):
        try:
            if self.quantity == 0:
                raise ZeroOrderProductQuantity(
                    "Товар с нулевым количеством не может быть добавлен."
                )
        except ZeroOrderProductQuantity as e:
            print(str(e))
        else:
            return f"Куплен товар {self.link} в количестве {self.quantity} на общую сумму {self.amount}."
        finally:
            print("Обработка заказа завершена.")

    def add_product(self, *args, **kwargs):
        return str(self)
