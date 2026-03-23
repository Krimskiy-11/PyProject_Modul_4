from src.product import Product


class Category:
    name: str
    description: str
    product: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = product

        Category.category_count += 1
        Category.product_count += len(product)

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self):
        try:
            total = 0
            for x in self.product_list:
                total += x.price * x.quantity
            return round(total / Category.product_count, 2)
        except ZeroDivisionError:
            print(0.0)

    @property
    def products(self):
        prod_list = ""
        for product in self.__products:
            prod_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return prod_list

    @property
    def product_list(self):
        product_list = []
        for product in self.__products:
            product_list.append(product)
        return product_list

    def __str__(self):
        full_quantity_products = 0
        for product in self.__products:
            full_quantity_products += product.quantity
        return f"{self.name}, количество продуктов: {full_quantity_products} шт."
