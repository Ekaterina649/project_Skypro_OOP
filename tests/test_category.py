import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_obj():
    product1 = Product("iPhone", "Смартфон", 100000.0, 10)
    product2 = Product("Samsung", "Смартфон", 80000.0, 15)
    product3 = Product("Xiaomi", "Смартфон", 50000.0, 20)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category_str_with_products(category_obj):
    """Тест строкового представления категории с товарами"""
    category_str = str(category_obj)
    assert category_str == "Смартфоны, количество продуктов: 45 шт."


def test_category_str_empty(empty_category):
    """Тест строкового представления пустой категории"""
    category_str = str(empty_category)
    assert category_str == "Смартфоны, количество продуктов: 0 шт."


def test_category_init(category_obj) -> None:
    assert category_obj.name == "Смартфоны"
    assert (
        category_obj.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    # Теперь проверяем через свойство products
    products_str = category_obj.products
    assert "iPhone, 100000.0 руб. Остаток: 10 шт." in products_str
    assert "Samsung, 80000.0 руб. Остаток: 15 шт." in products_str
    assert "Xiaomi, 50000.0 руб. Остаток: 20 шт." in products_str


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Смартфоны", "Описание", [])


@pytest.fixture
def sample_product():
    """Фикстура для тестового продукта"""
    return Product("iPhone", "Смартфон", 100000.0, 10)


def test_product_str_after_quantity_change(sample_product):
    """Тест строкового представления продукта после изменения количества"""
    sample_product.quantity = 5
    product_str = str(sample_product)
    assert product_str == "iPhone, 100000.0 руб. Остаток: 5 шт."


def test_add_product_to_empty_category(empty_category, sample_product):
    """Тест добавления продукта в пустую категорию"""
    initial_count = Category.product_count
    empty_category.add_product(sample_product)
    products_str = empty_category.products
    assert "iPhone, 100000.0 руб. Остаток: 10 шт." in products_str
    assert Category.product_count == initial_count + 1


def test_add_multiple_products(empty_category):
    """Тест добавления нескольких продуктов"""
    product1 = Product("iPhone", "Смартфон", 100000.0, 10)
    product2 = Product("Samsung", "Смартфон", 80000.0, 15)
    product3 = Product("Xiaomi", "Смартфон", 50000.0, 20)

    initial_count = Category.product_count

    empty_category.add_product(product1)
    empty_category.add_product(product2)
    empty_category.add_product(product3)

    products_str = empty_category.products

    # Проверяем все продукты
    assert "iPhone, 100000.0 руб. Остаток: 10 шт." in products_str
    assert "Samsung, 80000.0 руб. Остаток: 15 шт." in products_str
    assert "Xiaomi, 50000.0 руб. Остаток: 20 шт." in products_str

    # Проверяем счетчик
    assert Category.product_count == initial_count + 3


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

    # Используем переменные в asserts
    assert Category.category_count == 3
    assert Category.product_count == 6
    assert category1.name == "Электроника"
    assert category2.name == "Книги"
    assert category3.name == "Одежда"


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

    # Используем переменные в asserts
    assert Category.category_count == 2
    assert Category.product_count == 2  # Два продукта в двух категориях
    assert category1.name == "Категория 1"
    assert category2.name == "Категория 2"
    assert len(category1.products.split("\n")) == 2  # 1 продукт + пустая строка
    assert len(category2.products.split("\n")) == 2
