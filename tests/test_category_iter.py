import pytest

from src.category import Category
from src.category_iter import CategoryIterator
from src.product import Product


@pytest.fixture
def category_with_products() -> Category:
    """Фикстура для категории с товарами"""
    product1 = Product("iPhone", "Смартфон", 100000.0, 10)
    product2 = Product("Samsung", "Смартфон", 80000.0, 15)
    product3 = Product("Xiaomi", "Смартфон", 50000.0, 20)

    return Category("Смартфоны", "Описание категории", [product1, product2, product3])


@pytest.fixture
def empty_category() -> Category:
    """Фикстура для пустой категории"""
    return Category("Пустая категория", "Описание", [])


def test_iterator_creation(category_with_products: Category) -> None:
    """Тест создания итератора"""
    iterator = CategoryIterator(category_with_products)
    assert iterator is not None
    assert iterator.index == 0


def test_iterator_iter_method(category_with_products: Category) -> None:
    """Тест метода __iter__"""
    iterator = CategoryIterator(category_with_products)
    result = iterator.__iter__()
    assert result is iterator


def test_iterator_next_method(category_with_products: Category) -> None:
    """Тест метода __next__ с товарами"""
    iterator = CategoryIterator(category_with_products)

    product1 = iterator.__next__()
    assert product1.name == "iPhone"
    assert iterator.index == 1

    product2 = iterator.__next__()
    assert product2.name == "Samsung"
    assert iterator.index == 2

    product3 = iterator.__next__()
    assert product3.name == "Xiaomi"
    assert iterator.index == 3


def test_iterator_stop_iteration(category_with_products: Category) -> None:
    """Тест возникновения StopIteration"""
    iterator = CategoryIterator(category_with_products)

    for _ in range(3):
        iterator.__next__()

    with pytest.raises(StopIteration):
        iterator.__next__()


def test_iterator_empty_category(empty_category: Category) -> None:
    """Тест итератора для пустой категории"""
    iterator = CategoryIterator(empty_category)

    with pytest.raises(StopIteration):
        iterator.__next__()
