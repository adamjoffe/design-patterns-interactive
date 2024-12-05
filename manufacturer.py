from order import Order
from storage import Storage


class Manufacturer:
    storage: Storage

    def __init__(self):
        self.storage = Storage()

    def manufacture(self, order: Order) -> None:
        pass

    def ship_orders(self) -> None:
        pass
