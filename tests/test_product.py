import pytest

from src.product import Product
from src.smartphone import Smartphone


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
    with pytest.raises(ValueError,match='Товар с нулевым количеством не может быть добавлен'):
        product = Product("Товар", "Описание", 1000.0, 0)




def test_product_initialization_with_empty_strings() -> None:
    """Тест инициализации с пустыми строками"""
    product = Product("", "", 0.0, 10)

    assert product.name == ""
    assert product.description == ""
    assert product.price == 0.0

    assert product.quantity == 10


@pytest.fixture
def obj_product() -> Product:
    """Фикстура создания экземпляра продукта"""
    return Product("iphone", "Описание телефона", 1000000, 10)


@pytest.fixture
def obj_product_2() -> Product:
    """Фикстура создания экземпляра продукта"""
    return Product("samsung", "Описание2", 40000, 14)


@pytest.fixture
def obj_no_product() -> Product:
    """Фикстура создания экземпляра продукта"""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


def test_addit_class_object_product(obj_product: Product, obj_product_2: Product) -> None:
    """Тест, проверяющий корректное сложение объектов одного класса"""
    assert obj_product + obj_product_2 == 10560000


def test_addit_error(obj_product: Product, obj_no_product: Smartphone) -> None:
    """Тест, проверяющий, что возбуждается ошибка при сложении объектов разных классов"""
    with pytest.raises(TypeError):
        obj_product + obj_no_product


def test_str(obj_product: Product) -> None:
    """Проверяет, что выводится корректная строка"""
    product_str = str(obj_product)
    assert product_str == "iphone, 1000000 руб. Остаток: 10 шт."


def price_product(obj_product: Product) -> None:
    """Проверяет, что выводится корректная цена"""
    assert obj_product.price == 1000000


def test_product_price_setter_negative() -> None:
    """Тест установки невалидной цены через сеттер"""
    product = Product("Телефон", "Смартфон", 10000.0, 5)
    original_price = product.price

    # Пытаемся установить отрицательную цену
    product.price = -500.0
    assert product.price == original_price  # Цена не изменилась

    # Пытаемся установить нулевую цену
    product.price = 0.0
    assert product.price == original_price


def test_new_product_without_existing_products() -> None:
    """Тест создания нового продукта без существующих продуктов"""
    params = {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 50000.0, "quantity": 3}

    product = Product.new_product(params)

    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 50000.0
    assert product.quantity == 3


def test_new_product_with_existing_duplicate() -> None:
    """Тест создания продукта с дубликатом (обновление существующего)"""
    existing_products = [Product("Телефон", "Старое описание", 10000.0, 5)]

    params = {
        "name": "Телефон",  # Дубликат по имени
        "description": "Новое описание",
        "price": 12000.0,  # Более высокая цена
        "quantity": 3,  # Добавляемое количество
    }

    product = Product.new_product(params, existing_products)

    # Проверяем, что это тот же объект
    assert product is existing_products[0]
    assert product.name == "Телефон"
    assert product.description == "Новое описание"  # Описание обновилось
    assert product.price == 12000.0  # Цена обновилась (максимальная)
    assert product.quantity == 8
