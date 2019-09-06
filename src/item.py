class Item:
    def __init__(
        self, name, description,
        is_grabbable=True
    ):
        self.name = name
        self.description = description
        self.is_grabbable = is_grabbable

    def __getattr__(self, attr):
        return None

    def __str__(self):
        return (
            f"name: {self.name} | description: {self.description} | "
            f"is_grabbable: {self.is_grabbable}"
        )

    def __repr__(self):
        return (
            f"{type(self).__name__}({repr(self.name)}, "
            f"{repr(self.description)}, {repr(self.is_grabbable)})"
        )

    def on_take(self):
        print(
            f'\nYou picked up a {self.name}.\n' if self.is_grabbable
            else "\nYou are not allowed to grab that item.\n"
        )
        return self.is_grabbable

    def on_drop(self):
        print(f'\nYou dropped a {self.name}.\n')
