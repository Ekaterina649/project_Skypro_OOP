from typing import Dict, Any

import pytest

from src.base_product import BaseProduct
from src.product import Product


@pytest.fixture
def sample_product_params() -> Dict[str, Any]:
    """Фикстура с параметрами продукта"""
    return {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 1000.0,
        'quantity': 5
    }


@pytest.fixture
def test_product(sample_product_params) -> BaseProduct:
    """Фикстура для тестового продукта"""
    return Product(**sample_product_params)

def test_cannot_instantiate_base_product_directly():
    """Тест, что нельзя создать экземпляр абстрактного класса напрямую"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 1)

def test_base_product_initialization(test_product, sample_product_params):
    """Тест инициализации атрибутов базового продукта"""
    assert test_product.name == sample_product_params['name']
    assert test_product.description == sample_product_params['description']
    assert test_product.price == sample_product_params['price']
    assert test_product.quantity == sample_product_params['quantity']

def test_price_property_getter(test_product):
    """Тест геттера свойства price"""
    assert test_product.price == 1000.0
    assert isinstance(test_product.price, float)


def test_price_property_setter_valid(test_product):
    """Тест сеттера свойства price с валидным значением"""
    test_product.price = 1500.0
    assert test_product.price == 1500.0


def test_str_method_implementation(test_product):
    """Тест реализации метода __str__ в конкретном классе"""
    result = str(test_product)
    expected = "Test Product, 1000.0 руб. Остаток: 5 шт."
    assert result == expected


def test_add_method_same_type(test_product):
    """Тест метода __add__ с продуктом того же типа"""
    other_product = Product("Other Product", "Other Desc", 500.0, 3)

    result = test_product + other_product
    expected = (1000.0 * 5) + (500.0 * 3)  # 5000 + 1500 = 6500
    assert result == expected
    assert isinstance(result, float)


def test_new_product_class_method_new(sample_product_params):
    """Тест создания нового продукта через classmethod"""
    product = Product.new_product(sample_product_params)

    assert isinstance(product, Product)
    assert product.name == sample_product_params['name']
    assert product.description == sample_product_params['description']
    assert product.price == sample_product_params['price']
    assert product.quantity == sample_product_params['quantity']