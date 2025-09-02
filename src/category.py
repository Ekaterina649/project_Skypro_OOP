from src.product import Product


class Category:
    """Класс для описания категории продукта"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, new_product: Product) -> None:
        """Метод для добавления новых продуктов в категорию"""
        if not isinstance(new_product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products_list(self):
        """Геттер, возвращающий продукты относительно одной категории"""
        return self.__products

    def __str__(self) -> str:
        """Метод, возвращающий строковое представление категории продукта"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Возвращает строку со всеми продуктами категории в заданном формате"""
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result
