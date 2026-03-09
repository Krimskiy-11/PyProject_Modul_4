from src.category import Category
from src.product import Product


def test_category(first_category):

    # Функционал (урок 14.1)

    assert first_category.name == "Smartphones"
    assert first_category.description == ("Smartphones are not only a means of communication, "
                                          "but also provide additional features for a better life.")
    assert len(first_category.products.split("\n")) == 3

    assert first_category.category_count == 1
    assert first_category.product_count == 2

    # Функционал (урок 14.2)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    first_category.add_product(product4)
    assert len(first_category.products.split("\n")) == 4

    assert first_category.product_count == 3
    