def test_product(first_product):
    assert first_product.name == "IPhone 15 Pro"
    assert first_product.description == "128GB, White"
    assert first_product.price == 105_000
    assert first_product.quantity == 1
