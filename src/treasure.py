from item import Item


class Treasure(Item):
    def __init__(
        self, name, description,
        is_grabbable=True
    ):
        super().__init__(name, description, is_grabbable)

    def __getattr__(self, attr):
        return None

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()
