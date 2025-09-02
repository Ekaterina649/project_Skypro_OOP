import pytest

from src.lawn_grass import LawnGrass
from src.product import Product


@pytest.fixture
def lawn_grass_product():
    """Фикстура для продукта LawnGrass"""
    return LawnGrass(
        name="Газонная трава Premium",
        description="Высококачественная газонная трава",
        price=1500.0,
        quantity=100,
        country="Россия",
        germination_period="14 дней",
        color="зеленый",
    )


@pytest.fixture
def another_lawn_grass():
    """Фикстура для другого продукта LawnGrass"""
    return LawnGrass(
        name="Газонная трава Standard",
        description="Стандартная газонная трава",
        price=1000.0,
        quantity=50,
        country="Беларусь",
        germination_period="21 день",
        color="темно-зеленый",
    )


def test_lawn_grass_inheritance(lawn_grass_product):
    """Тест наследования от класса Product"""
    assert isinstance(lawn_grass_product, Product)
    assert isinstance(lawn_grass_product, LawnGrass)


def test_lawn_grass_attributes(lawn_grass_product):
    """Тест атрибутов класса LawnGrass"""
    assert lawn_grass_product.name == "Газонная трава Premium"
    assert lawn_grass_product.description == "Высококачественная газонная трава"
    assert lawn_grass_product.price == 1500.0
    assert lawn_grass_product.quantity == 100
    assert lawn_grass_product.country == "Россия"
    assert lawn_grass_product.germination_period == "14 дней"
    assert lawn_grass_product.color == "зеленый"


def test_lawn_grass_addition_same_type(lawn_grass_product, another_lawn_grass):
    """Тест сложения двух объектов LawnGrass"""
    total_cost = lawn_grass_product + another_lawn_grass

    expected_cost = (
        lawn_grass_product.quantity * lawn_grass_product.price + another_lawn_grass.quantity * another_lawn_grass.price
    )

    assert total_cost == expected_cost
    assert total_cost == (100 * 1500.0 + 50 * 1000.0)
    assert total_cost == 200000.0


def test_lawn_grass_addition_different_type_error(lawn_grass_product):
    """Тест ошибки при сложении с объектом другого типа"""
    regular_product = Product("Обычный товар", "Описание", 1000.0, 10)

    with pytest.raises(TypeError, match="Объект не является объектом класса LawnGrass"):
        lawn_grass_product + regular_product


def test_lawn_grass_addition_with_int_error(lawn_grass_product):
    """Тест ошибки при сложении с числом"""
    with pytest.raises(TypeError, match="Объект не является объектом класса LawnGrass"):
        lawn_grass_product + 100
