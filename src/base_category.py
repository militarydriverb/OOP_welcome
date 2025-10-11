from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """Создание абстрактного класса BaseCategory"""

    @classmethod
    @abstractmethod
    def __init__(cls, *args, **kwargs):
        """Создание абстрактного метода __init__"""
        pass
