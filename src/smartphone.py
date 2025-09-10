from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other) -> float:
        """Метод, складывающий стоимость товаров на складе"""
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError("Объект не является объектом класса Smartphone")
