from src.product import Product


def test_product_initialization_with_valid_data() -> None:
    """Тест корректной инициализации продукта с валидными данными"""
    product = Product("Телефон", "Смартфон", 10000.0, 5)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 10000.0
    assert product.quantity == 5


def test_product_initialization_with_different_data_types() -> None:
    """Тест инициализации с разными типами данных"""
    # Числа как целые и float
    product1 = Product("Товар 1", "Описание 1", 100, 10)  # int price
    product2 = Product("Товар 2", "Описание 2", 99.99, 5)  # float price

    assert product1.price == 100
    assert product2.price == 99.99
    assert isinstance(product1.price, int)
    assert isinstance(product2.price, float)


def test_product_initialization_with_zero_quantity() -> None:
    """Тест инициализации с нулевым количеством"""
    product = Product("Товар", "Описание", 1000.0, 0)

    assert product.quantity == 0
    assert product.name == "Товар"
    assert product.price == 1000.0


def test_product_initialization_with_empty_strings() -> None:
    """Тест инициализации с пустыми строками"""
    product = Product("", "", 0.0, 0)

    assert product.name == ""
    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0
