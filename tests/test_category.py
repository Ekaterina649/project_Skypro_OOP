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

    # Теперь проверяем через свойство products_list (а не products)
    products_list = category_obj.products_list
    assert len(products_list) == 3
    assert products_list[0].name == "iPhone"
    assert products_list[1].name == "Samsung"
    assert products_list[2].name == "Xiaomi"


@pytest.fixture
def empty_category() -> Category:
    """Фикстура для пустой категории"""
    return Category("Смартфоны", "Описание", [])


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для тестового продукта"""
    return Product("iPhone", "Смартфон", 100000.0, 10)


@pytest.fixture
def another_product() -> Product:
    """Фикстура для другого тестового продукта"""
    return Product("Samsung", "Смартфон", 80000.0, 15)


def test_add_product_valid(empty_category: Category, sample_product: Product) -> None:
    """Тест добавления корректного продукта в категорию"""
    initial_product_count = Category.product_count
    initial_category_products = len(empty_category.products_list)

    # Добавляем продукт
    empty_category.add_product(sample_product)

    # Проверяем, что продукт добавлен в список категории
    assert len(empty_category.products_list) == initial_category_products + 1
    assert empty_category.products_list[-1] == sample_product

    # Проверяем, что счетчик продуктов увеличился
    assert Category.product_count == initial_product_count + 1


def test_add_product_invalid_type(empty_category: Category) -> None:
    """Тест добавления объекта неверного типа"""
    invalid_product = "не продукт"

    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        empty_category.add_product(invalid_product)

    # Проверяем, что список продуктов не изменился
    assert len(empty_category.products_list) == 0


def test_product_str_after_quantity_change(sample_product: Product) -> None:
    """Тест строкового представления продукта после изменения количества"""
    sample_product.quantity = 5
    product_str = str(sample_product)
    assert product_str == "iPhone, 100000.0 руб. Остаток: 5 шт."


def test_add_product_to_empty_category(empty_category: Category, sample_product: Product) -> None:
    """Тест добавления продукта в пустую категорию"""
    initial_count = Category.product_count
    empty_category.add_product(sample_product)

    # Проверяем, что продукт добавлен в список
    products_list = empty_category.products_list
    assert len(products_list) == 1
    assert products_list[0].name == "iPhone"
    assert Category.product_count == initial_count + 1


def test_add_multiple_products(empty_category: Category) -> None:
    """Тест добавления нескольких продуктов"""
    product1 = Product("iPhone", "Смартфон", 100000.0, 10)
    product2 = Product("Samsung", "Смартфон", 80000.0, 15)
    product3 = Product("Xiaomi", "Смартфон", 50000.0, 20)

    initial_count = Category.product_count

    empty_category.add_product(product1)
    empty_category.add_product(product2)
    empty_category.add_product(product3)

    products_list = empty_category.products_list

    # Проверяем все продукты
    assert len(products_list) == 3
    assert products_list[0].name == "iPhone"
    assert products_list[1].name == "Samsung"
    assert products_list[2].name == "Xiaomi"

    # Проверяем счетчик
    assert Category.product_count == initial_count + 3


def test_initial_counters_zero() -> None:
    """Тест, что начальные значения счетчиков равны 0"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0


def test_multiple_categories_counters() -> None:
    """Тест подсчета для нескольких категорий"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем несколько категорий с продуктами
    product1 = Product("Телевизор", "Электроника", 50000.0, 5)
    product2 = Product("Наушники", "Электроника", 10000.0, 8)

    category1 = Category("Электроника", "Электронные устройства", [product1, product2])
    category2 = Category("Книги", "Книги и журналы", [])
    category3 = Category("Одежда", "Одежда и аксессуары", [])

    # Проверяем счетчики
    assert Category.category_count == 3
    assert Category.product_count == 2  # Только 2 продукта в первой категории


@pytest.fixture
def empty_category_params():
    """Фикстура с параметрами для пустой категории"""
    return ("Пустая категория", "Описание пустой категории", [])


def test_empty_category_counter(empty_category_params) -> None:
    """Тест подсчета для пустой категории"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    name, description, products = empty_category_params
    category = Category(name, description, products)

    assert Category.category_count == 1
    assert Category.product_count == 0
    assert len(category.products_list) == 0


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

    # Проверяем счетчики
    assert Category.category_count == 2
    assert Category.product_count == 2  # Два продукта в двух категориях
    assert category1.name == "Категория 1"
    assert category2.name == "Категория 2"
    assert len(category1.products_list) == 1
    assert len(category2.products_list) == 1


def test_category_len_method(category_obj, empty_category):
    """Тест метода __len__ для категории"""
    # Для категории с товарами
    assert len(category_obj) == 3  # Количество продуктов в списке

    # Для пустой категории
    assert len(empty_category) == 0  # Пустой список продуктов