class Item:
    def __init__(
        self, name, description,
        is_grabbable=True, is_win_condition=False
    ):
        self.name = name
        self.description = description
        self.is_grabbable = is_grabbable
        self.is_win_condition = is_win_condition

    def __getattr__(self, attr):
        return None

    def on_take(self):
        print(
            f'\nYou picked up a {self.name}.\n' if self.is_grabbable
            else "\nYou are not allowed to grab that item.\n"
        )
        return (self.is_grabbable, self.is_win_condition)

    def on_drop(self):
        print(f'\nYou dropped a {self.name}.\n')
