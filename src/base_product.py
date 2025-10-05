from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Создание абстрактного класса BaseProduct"""

    @classmethod
    @abstractmethod
    def __init__(cls, *args, **kwargs):
        """Создание абстрактного метода __init__"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Создание абстрактного метода new_product"""
        pass

    @classmethod
    @abstractmethod
    def __add__(cls, *args, **kwargs):
        """Создание абстрактного метода __add__"""
        pass
