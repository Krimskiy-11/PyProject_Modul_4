import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product(
        name="IPhone 15 Pro", description="128GB, White", price=105_000, quantity=1
    )


@pytest.fixture
def first_category():
    return Category(
        name="Smartphones",
        description="Smartphones are not only a means of communication, "
        "but also provide additional features for a better life.",
        product=[
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
        ],
    )
