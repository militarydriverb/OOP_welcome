class PrintMixin:
    """Создание класса PrintMixin"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.discription}, {self.price}, {self.quantity})"
