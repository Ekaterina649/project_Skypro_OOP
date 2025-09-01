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
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со всеми продуктами категории в заданном формате"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
