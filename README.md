# Python Project OOP
## Описание проекта
Проект по объектно-ориентированному программированию на Python, реализующий систему управления товарами и категориями
## Структура проекта
* src/ -папка, где находятся основные модули
* src/category.py - модуль, где находится класс с описанием категории продукта
* src/product.py - модуль, где находится класс с описанием продукта
* src/category_iter.py - модуль, где находится класс, в котором можно перебирать товары одной категории
* src/lawn_grass.py - модуль с классом Lawn_grass, который наследуется от класса Product, находящийся в модуле product.py
* src/smartphone.py - модуль с классом Smartphone, который наследуется от класса Product, находящийся в модуле product.py
* src/base_product - модуль с классом BaseProduct, от которого наследуется класс  Product
* rsc/print_mixin - миксин PrintMixin для вывода информации о создании объектов


* tests/ - папка с тестами проекта
* tests/test_base_product.py - тесты абстрактного базового класса
* tests/test_category.py - тестирование модуля category.py
* tests/test_product.py - тестирование модуля product.py
* tests/test_smartphone.py - тестирование модуля smartphone.py
* tests/test_lawn_grass.py - тестирование модуля lawn_grass.py
* tests/test_print_mixin.py - тесты миксина PrintMixin

* poetry.lock - зависимости проекта

## Установка
Склонируйте репозиторий:


`git clone git@github.com:Ekaterina649/project_Skypro_OOP.git`

## Установка и запуск
Для того, чтобы запустить проект сначала нужно установить зависимости.

`poetry install`

## Запуск тестов
Для запуска всех тестов:
`pytest`

Для генерации HTML отчета о покрытии:

`pytest --cov=src --cov-report=html`

## Основные классы

### BaseProduct (Абстрактный класс)
* Определяет общий интерфейс для всех продуктов
* Содержит абстрактные методы: __str__, __add__, new_product
* Реализует общую логику для цены с валидацией

### Product (Базовый класс товара)
* Наследует BaseProduct и PrintMixin
* Управление основными свойствами товара: название, описание, цена, количество
* Валидация цены
* Перегрузка операторов для математических операций

### Category (Категория товаров)
* Управление коллекцией товаров
* Подсчет общего количества товаров в категории
* Добавление новых товаров с проверкой типа

### Smartphone (Наследник Product)
* Дополнительные атрибуты: эффективность, модель, память, цвет
* Специфическая логика сложения стоимости

### LawnGrass (Наследник Product)
* Дополнительные атрибуты: страна-производитель, срок прорастания, цвет
* Специфическая логика сложения стоимости

### CategoryIterator (Итератор категорий)
* Позволяет перебирать товары в категории

### PrintMixin (Миксин)
* Добавляет функционал вывода информации при создании объектов
* Автоматически выводит repr объекта при инициализации

## Пример использования
```
    if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)`
