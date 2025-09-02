import pytest

from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def smartphone_product():
    """Фикстура для продукта Smartphone"""
    return Smartphone(
        name="iPhone 15",
        description="Флагманский смартфон",
        price=100000.0,
        quantity=50,
        efficiency="Высокая",
        model="15 Pro",
        memory="256GB",
        color="черный",
    )


@pytest.fixture
def another_smartphone():
    """Фикстура для другого продукта Smartphone"""
    return Smartphone(
        name="Samsung Galaxy",
        description="Android смартфон",
        price=80000.0,
        quantity=30,
        efficiency="Средняя",
        model="S23",
        memory="128GB",
        color="синий",
    )


def test_smartphone_inheritance(smartphone_product):
    """Тест наследования от класса Product"""
    assert isinstance(smartphone_product, Product)
    assert isinstance(smartphone_product, Smartphone)


def test_smartphone_attributes(smartphone_product):
    """Тест атрибутов класса Smartphone"""
    assert smartphone_product.name == "iPhone 15"
    assert smartphone_product.description == "Флагманский смартфон"
    assert smartphone_product.price == 100000.0
    assert smartphone_product.quantity == 50
    assert smartphone_product.efficiency == "Высокая"
    assert smartphone_product.model == "15 Pro"
    assert smartphone_product.memory == "256GB"
    assert smartphone_product.color == "черный"


def test_smartphone_addition_same_type(smartphone_product, another_smartphone):
    """Тест сложения двух объектов Smartphone"""
    total_cost = smartphone_product + another_smartphone

    expected_cost = (
        smartphone_product.quantity * smartphone_product.price + another_smartphone.quantity * another_smartphone.price
    )

    assert total_cost == expected_cost
    assert total_cost == (50 * 100000.0 + 30 * 80000.0)
    assert total_cost == 7400000.0


def test_smartphone_addition_different_type_error(smartphone_product):
    """Тест ошибки при сложении с объектом другого типа"""
    regular_product = Product("Обычный товар", "Описание", 1000.0, 10)

    with pytest.raises(TypeError, match="Объект не является объектом класса Smartphone"):
        smartphone_product + regular_product


def test_smartphone_addition_with_int_error(smartphone_product):
    """Тест ошибки при сложении с числом"""
    with pytest.raises(TypeError, match="Объект не является объектом класса Smartphone"):
        smartphone_product + 100
