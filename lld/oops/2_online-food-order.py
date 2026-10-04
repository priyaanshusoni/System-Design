# A Order class managing food delivery orders


class Order:

    def __init__(self, order_id: str, customer_id: str) -> None:
        self._order_id = order_id
        self._customer_id = customer_id
        self._items: list[tuple[str, float]] = []
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

    @property
    def total_amount(self) -> float:
        total = 0
        for name, price in self._items:
            total += price

        return total

    def add_item(self, name: str, price: float) -> None:
        if self._is_placed:
            raise RuntimeError("Cannot modify a placed order.")

        self._items.append((name, price))

    def place_order(self) -> bool:
        if not self._items:
            raise RuntimeError("Please Add items to place an order")
        elif self._is_placed:
            raise RuntimeError("Order is already placed")

        self._is_placed = True

        return True

    def get_items_count(self) -> int:
        return len(self._items)

    def display_order(self):
        status = "PLACED" if self._is_placed else "PENDING"

        print(f"Order {self._order_id} for {self._customer_id} is {status}")
        for name, price in self._items:
            print(f"- {name} - {price}  ")

        print(f"Total : {self.total_amount :.2f}")


if __name__ == "__main__":

    order1 = Order("ORD-001", "UID1234")

    order1.display_order()
    print(order1.get_items_count())
    order1.add_item(name="Pizza", price=349.00)
    order1.add_item(name="Garlic Bread", price=49.00)
    print(order1.items)

    order1.display_order()
    print(order1._order_id)

    order1.items.append(("Free Burger", 0))
    print(order1.get_items_count())

    order1.place_order()

    try:
        order1.add_item("Coke", 60)
    except RuntimeError as e:
        print(f"Failed {e}")

    order2 = Order(order_id="OID343", customer_id="UID433")

    try:
        order2.place_order()
    except RuntimeError as e:
        print(f"Failed {e}")

    order2.add_item("Lays", 20.00)
    order2.place_order()

    try:
        order2.place_order()
    except RuntimeError as e:
        print(f"Failed {e}")
