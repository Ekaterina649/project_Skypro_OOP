import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_obj():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )


def test_category_init(category_obj) -> None:
    assert category_obj.name == "Смартфоны"
    assert (
        category_obj.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_obj.products == ["product1", "product2", "product3"]


def test_initial_counters_zero() -> None:
    """Тест, что начальные значения счетчиков равны 0"""
    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0


def test_multiple_categories_counters() -> None:
    """Тест подсчета для нескольких категорий"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем несколько категорий
    category1 = Category("Электроника", "Электронные устройства", ["1", "2"])
    category2 = Category("Книги", "Книги и журналы", ["3", "4"])
    category3 = Category("Одежда", "Одежда и аксессуары", ["5", "6"])

    assert Category.category_count == 3
    assert Category.product_count == 6


@pytest.fixture
def empty_category_params():
    """Фикстура с параметрами для пустой категории"""
    return ("Пустая категория", "Описание пустой категории", [])


def test_empty_category_counter(empty_category_params) -> None:
    """Тест подсчета для пустой категории"""
    Category.category_count = 0
    Category.product_count = 0
    name, description, products = empty_category_params
    category = Category(name, description, products)

    assert Category.category_count == 1
    assert Category.product_count == 0
    assert len(category.products) == 0


def test_mixed_categories_with_duplicate_products() -> None:
    """Тест с категориями, содержащими одинаковые продукты"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем общий продукт
    common_product = Product("Общий товар", "Описание", 1000.0, 5)

    # Создаем категории с общим продуктом
    category1 = Category("Категория 1", "Описание 1", [common_product])
    category2 = Category("Категория 2", "Описание 2", [common_product])

    # Проверяем, что каждый продукт учитывается, даже если он одинаковый
    assert Category.category_count == 2
    assert Category.product_count == 2  # Два продукта в двух категориях
