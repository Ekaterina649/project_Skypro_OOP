class CategoryIterator:
    """Итератор для перебора товаров внутри категории"""

    def __init__(self, category):
        self._products = category.products_list
        self.index = 0

    def __iter__(self):
        """Возвращает итератор"""
        return self

    def __next__(self):
        """Метод, возвращающий следующий элемент спсика"""
        if self.index < len(self._products):
            product = self._products[self.index]
            self.index += 1
            return product
        raise StopIteration
