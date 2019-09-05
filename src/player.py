class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __getattr__(self, attr):
        return None

    def show_location(self):
        self.current_room.show_overview()

    def move_to_room(self, room):
        if room is None:
            print("\nYou cannot move in that direction right now.\n")
        else:
            self.current_room = room
            self.show_location()

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        if len(self.items) == 0:
            print("\nYour inventory is currently empty.\n")
        else:
            print("\nYour current inventory:\n")
            for item in self.items:
                print(f"{item.name} - {item.description}")

    def take_item(self, target):
        for item in self.current_room.items:
            if item.name == target:
                self.items.append(item)
                item.on_take()
                return
        print("\nNo such item in this room\n")
