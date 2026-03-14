from src.category import Category


class Iterator:

    def __init__(self, category_object: Category):
        self.object = category_object
        self.stop = len(category_object.product_list)

    def __iter__(self) -> "Iterator":
        self.value = -1
        return self

    def __next__(self) -> str:
        if self.value + 1 < self.stop:
            self.value += 1
            return str(self.object.product_list[self.value])
        else:
            raise StopIteration

    def __getitem__(self, item):
        return str(self.object.product_list[item])
