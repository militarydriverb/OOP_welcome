from src.base_category import BaseCategory


class Order(BaseCategory):

    def __init__(self, link, quantity, price):
        self.link = link
        self.quantity = quantity
        self.price = price
        self.amount = self.quantity * self.price

    def __str__(self):
        return f"Куплен товар {self.link} в количестве {self.quantity} на общую сумму {self.amount}."

    def add_product(self, *args, **kwargs):
        return str(self)
