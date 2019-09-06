from item import Item


class Weapon(Item):
    def __init__(self, name, description, ap):
        super().__init__(name, description)
        self.ap = ap
