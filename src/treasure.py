from item import Item


class Treasure(Item):
    def __init__(
        self, name, description,
        is_grabbable=True
    ):
        super().__init__(name, description, is_grabbable)
