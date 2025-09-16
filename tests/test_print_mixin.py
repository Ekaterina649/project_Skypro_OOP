import pytest
from src.product import Product
from src.lawn_grass import LawnGrass
from src.smartphone import Smartphone


def test_print_mixin_with_product(capsys):
    """Тест миксина с классом Product"""
    product = Product("iPhone", "Смартфон", 100000.0, 10)

    captured = capsys.readouterr()
    expected_output = "Product('iPhone', 'Смартфон', 100000.0, 10)"
    assert captured.out.strip() == expected_output


def test_print_mixin_with_lawn_grass(capsys):
    """Тест миксина с классом LawnGrass"""
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Качественная газонная трава",
        500.0,
        20,
        "Россия",
        "14 дней",
        "зеленый"
    )

    captured = capsys.readouterr()
    expected_output = "LawnGrass('Газонная трава', 'Качественная газонная трава', 500.0, 20)"
    assert captured.out.strip() == expected_output


def test_print_mixin_with_smartphone(capsys):
    """Тест миксина с классом Smartphone"""
    smartphone = Smartphone(
        "Samsung Galaxy",
        "Флагманский смартфон",
        80000.0,
        15,
        "Высокая",
        "Galaxy S23",
        "256GB",
        "черный"
    )

    captured = capsys.readouterr()
    expected_output = "Smartphone('Samsung Galaxy', 'Флагманский смартфон', 80000.0, 15)"
    assert captured.out.strip() == expected_output