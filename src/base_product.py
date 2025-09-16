from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер, возвращающий цену продукта"""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер, устанавливающий новую цену продукта"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        """Метод, складывающий стоимость товаров на складе"""
        pass

    @classmethod
    @abstractmethod
    def new_product(
        cls, params_product: Dict[str, Any], existing_products: Optional[List["BaseProduct"]] = None
    ) -> "BaseProduct":
        """Метод, создающий новый продукт или обновляющий существующий при наличии дубликата"""
        pass
