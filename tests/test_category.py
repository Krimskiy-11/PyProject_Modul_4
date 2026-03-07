def test_category(first_category):
    assert first_category.name == "Smartphones"
    assert first_category.description == ("Smartphones are not only a means of communication, "
                                          "but also provide additional features for a better life.")
    assert len(first_category.products) == 2

    assert first_category.category_count == 1
    assert first_category.product_count == 2
