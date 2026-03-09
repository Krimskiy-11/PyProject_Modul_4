from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = product

        Category.category_count += 1
        Category.product_count += len(product)

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        self.product_count += 1

    @property
    def products(self):
        prod_list = ""
        for product in self.__products:
            prod_list += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return prod_list





