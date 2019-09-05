class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __getattr__(self, attr):
        return None

    def on_take(self):
        print(f'\nYou picked up a {self.name}.\n')

    def on_drop(self):
        print(f'\nYou dropped a {self.name}.\n')
