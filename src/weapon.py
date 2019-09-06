from item import Item


class Weapon(Item):
    def __init__(self, name, description, ap):
        super().__init__(name, description)
        self.ap = ap

    def __getattr__(self, attr):
        return None

    def __str__(self):
        return f"{super().__str__()} | ap: {self.ap}"

    def __repr__(self):
        return (
            f"{type(self).__name__}({repr(self.name)}, "
            f"{repr(self.description)}, {repr(self.is_grabbable)}, "
            f"{repr(self.ap)})"
        )
