class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        print("Your current inventory:")
        for item in self.items:
            print(f"{item.name} - {item.description}")
