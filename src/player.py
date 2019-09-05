class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __getattr__(self, attr):
        return None

    def move_to_room(self, room):
        if room is None:
            print("You cannot move in that direction right now.")
        else:
            self.current_room = room

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        print("Your current inventory:")
        if len(self.items) == 0:
            print("Your inventory is empty.")
        else:
            for item in self.items:
                print(f"{item.name} - {item.description}")
