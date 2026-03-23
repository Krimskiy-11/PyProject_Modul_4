import pytest

from src.product import Product, Smartphone, LawnGrass
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


@pytest.fixture
def first_phone():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def second_phone():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture
def first_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def second_grass():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
