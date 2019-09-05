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
            print("\nYour current inventory:")
            for item in self.items:
                print(f"    - {item.name} ({item.description})")
            print()

    def take_item(self, target):
        for item in self.current_room.items:
            if item.name == target:
                item.on_take()
                self.items.append(item)
                return
        print("\nNo such item in this room.\n")

    def drop_item(self, target):
        for i in range(len(self.items)):
            if self.items[i].name == target:
                self.items[i].on_drop()
                del self.items[i]
                return
        print("\nYou do not currently have that item.\n")
