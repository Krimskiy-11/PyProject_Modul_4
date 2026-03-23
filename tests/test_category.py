from src.category import Category
from src.product import Product


def test_category(first_category, first_phone, second_phone):

    # Функционал (урок 14.1)

    assert first_category.name == "Smartphones"
    assert first_category.description == (
        "Smartphones are not only a means of communication, "
        "but also provide additional features for a better life."
    )
    assert len(first_category.products.split("\n")) == 3

    assert first_category.category_count == 1
    assert first_category.product_count == 2

    # Функционал (урок 14.2)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    first_category.add_product(product4)
    assert len(first_category.products.split("\n")) == 4

    assert first_category.product_count == 3

    # Функционал (урок 15.1)

    assert str(first_category) == "Smartphones, количество продуктов: 20 шт."

    # Функционал (урок 16.1)

    first_category.add_product(first_phone)
    first_category.add_product(second_phone)
    assert Category.product_count == 5

    try:
        first_category.add_product("No product")
    except TypeError:
        print("Ошибка")
    else:
        assert Category.product_count == 6

    # Функционал (урок 17.1)

    assert first_category.middle_price() == 1111000.0

    category_empty = Category("Пустая категория", "Категория без продуктов", [])

    assert category_empty.middle_price() == 0.0
