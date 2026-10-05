# MAke everything private by default then selectively expose what needs to be public


from multiprocessing import Value


class Product:

    def __init__(self, name, price) -> None:
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


p1 = Product(name="Shirt", price=499)


print(p1.get_name())
print(p1.get_price())


# Getters and Setters


class Product2:

    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")

        self.__price = value


p2 = Product2(name="ABC", price=-399.00)  # will throw error
