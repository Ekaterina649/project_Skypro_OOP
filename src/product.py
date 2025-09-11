from typing import Any, Dict, List, Optional

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        BaseProduct.__init__(self, name, description, price, quantity)
        PrintMixin.__init__(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Метод, складывающий стоимость товаров на складе"""
        if type(other) is type(self):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError("Объект не является объектом класса Product")

    @classmethod
    def new_product(
        cls, params_product: Dict[str, Any], existing_products: Optional[List["Product"]] = None
    ) -> "Product":
        """Метод, создающий новый продукт или обновляющий существующий при наличии дубликата"""
        name = params_product.get("name")
        description = params_product.get("description")
        price = params_product.get("price")
        quantity = params_product.get("quantity")
        if existing_products:
            for existing_product in existing_products:
                if existing_product.name.lower() == name.lower():
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    if description:
                        existing_product.description = description
                    return existing_product

        # Если дубликат не найден - создаем новый продукт
        return cls(name, description, price, quantity)
