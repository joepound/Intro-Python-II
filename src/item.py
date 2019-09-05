class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __getattr__(self, attr):
        return None

    def on_take(self):
        print(f'You picked up "{self.name}".')

    def on_drop(self):
        print(f'You dropped "{self.name}".')
