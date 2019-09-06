from item import Item


class LightSource(Item):
    def __init__(
        self, name, description,
        is_grabbable=True
    ):
        super().__init__(name, description)

    def __getattr__(self, attr):
        return None

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def on_drop(self):
        super().on_drop()
        print("It is not wise to drop your source of light!\n")
