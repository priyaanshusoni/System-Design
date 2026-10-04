# A Order class managing food delivery orders


class Order:

    def __init__(self, order_id: str, customer_id: str) -> None:
        self._order_id = order_id
        self._customer_id = customer_id
        self._items: list[tuple[str, float]] = []
        self._total_amount = 0
        self._is_placed = False

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def customer_id(self) -> str:
        return self._customer_id

    @property
    def is_placed(self) -> bool:
        return self._is_placed

    @property
    def items(self) -> list:
        copy = list(self._items)
        return copy

    def add_item(self, name: str, price: float) -> None:
        if self._is_placed:
            print("Cannot Modify the placed order.")
            return

        self._items.append((name, price))
        self._total_amount += price

    def place_order(self) -> bool:
        if self._is_placed or not self._items:
            return False
        self._is_placed = True

        return True

    def get_items_count(self) -> int:
        return len(self._items)

    def display_order(self):
        status = "PLACED" if self._is_placed else "PENDING"

        print(f"Order {self._order_id} for {self._customer_id} is {status}")
        for item in self._items:
            print(f"- {item} -  ")

        print(f"Total : {self._total_amount :.2f}")


order1 = Order("ORD-001", "UID1234")


order1.display_order()
print(order1.get_items_count())
order1.add_item(name="Pizza", price=349.00)
order1.add_item(name="Garlic Bread", price=49.00)
print(order1.items)


print(order1._order_id)


order1.items.append(("Free Burger", 0))
print(order1.get_items_count())
