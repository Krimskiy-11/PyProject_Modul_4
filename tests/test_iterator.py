from src.iterator import Iterator


def test_iterator(first_category):
    phones_iterator = Iterator(first_category)
    assert next(iter(phones_iterator)) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."

    assert phones_iterator[0] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
