from typing import Any, Dict, List, Optional


class Product:
    """Класс для описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер, возвращающий цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер, устанавливающий новую цену продукта"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Метод, складывающий стоимость товаров на складе"""
        return self.quantity * self.price + other.quantity * other.price

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
