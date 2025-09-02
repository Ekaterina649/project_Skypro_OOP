from src.product import Product


class LawnGrass(Product):
    def __init__(self,name, description, price, quantity,country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period= germination_period
        self.color= color

    def __add__(self, other) -> float:
        """Метод, складывающий стоимость товаров на складе"""
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError("Объект не является объектом класса LawnGrass")


