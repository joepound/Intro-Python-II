from item import Item


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        super().on_drop()
        print("It is not wise to drop your source of light!\n")
