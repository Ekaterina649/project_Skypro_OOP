from src.product import Product
from src.exceptions import ZeroQuantityCategory

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
        try:
            if new_product.quantity == 0:
                raise ZeroQuantityCategory ("Нельзя добавить товар в категорию с нулевым количеством")
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                print(f"Товар '{new_product.name}' успешно добавлен в категорию '{self.name}'")
        except ZeroQuantityCategory as e:
            print(str(e))
        finally:
            print("Обработка добавления товара завершена")

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
        return self.__products

    def __len__(self):
        """Позволяет использовать len(category) для подсчёта товаров"""
        return len(self.__products)

    def middle_price(self):
        try:
            if len(self.__products) == 0:
                return 0
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0



