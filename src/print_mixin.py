class PrintMixin:
    """Миксин для вывода информации о создании объекта"""

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def print_info(self):
        """Метод для явного вывода информации"""
        print(repr(self))
