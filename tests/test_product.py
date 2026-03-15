from src.product import Product


def test_product(first_product, first_phone, second_phone, first_grass, second_grass):

    # Функционал (урок 14.1.)

    assert first_product.name == "IPhone 15 Pro"
    assert first_product.description == "128GB, White"
    assert first_product.price == 105_000
    assert first_product.quantity == 1

    # Функционал (урок 14.2.)

    second_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert second_product.name == "Samsung Galaxy S23 Ultra"
    assert second_product.description == "256GB, Серый цвет, 200MP камера"
    assert second_product.price == 180000.0
    assert second_product.quantity == 5

    second_product.price = 11_000
    assert second_product.price == 11_000

    second_product.price = -12
    assert second_product.price == 11_000

    second_product.price = 0
    assert second_product.price == 11_000

    # Функционал (урок 15.1.)

    assert str(first_product) == "IPhone 15 Pro, 105000 руб. Остаток: 1 шт."
    assert first_product + second_product == 160000

    # Функционал (урок 16.1.)

    sum_product_phones = first_phone + second_phone
    sum_product_grasses = first_grass + second_grass
    assert sum_product_phones == 2114000
    assert sum_product_grasses == 16750

    try:
        error_sum = first_phone + first_grass
    except TypeError:
        print("Ошибка")
    else:
        assert error_sum == 116000
