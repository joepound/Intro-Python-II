from lightsource import LightSource


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.has_light_source = False

    def __getattr__(self, attr):
        return None

    def show_location(self):
        self.current_room.show_overview(self.has_light_source)

    def move_to_room(self, room):
        if room is None:
            print("\nYou cannot move in that direction right now.\n")
        else:
            self.current_room = room
            self.current_room.show_overview(self.has_light_source)

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
        if self.current_room.is_light or self.has_light_source:
            for item in self.current_room.items:
                if item.name == target and item.on_take():
                    if isinstance(item, LightSource):
                        self.has_light_source = True
                    self.items.append(item)
                return
            print("\nNo such item in this room.\n")
        else:
            print("\nGood luck finding that in the dark!\n")

    def drop_item(self, target):
        has_found_item = False
        has_dropped_light_source = False
        for i in range(len(self.items)):
            if self.items[i].name == target:
                self.items[i].on_drop()
                if isinstance(self.items[i], LightSource):
                    has_dropped_light_source = True
                del self.items[i]
                has_found_item = True
                break
        if not has_found_item:
            print("\nYou do not currently have that item.\n")
        elif has_dropped_light_source:
            has_other_light_source = False
            for i in range(len(self.items)):
                if isinstance(self.items[i], LightSource):
                    has_other_light_source = True
                    break
            if not has_other_light_source:
                self.has_light_source = False

    def attack(self, target):
        if self.current_room.is_light or self.has_light_source:
            for monster in self.current_room.monsters:
                if monster.name == target:
                    # Arbitrary attack power value to be changed for weapons
                    print(f"\nYou raise your fists and attack the monster!\n")
                    monster.on_attack(20)
                    return
            print("\nNo such monster in the current room.\n")
        else:
            print(
                "\nTry as you might, you are unable to attack accurately in "
                "the dark!\n"
            )
