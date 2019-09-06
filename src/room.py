class Room:
    # Same directional order for adjacent rooms as CSS TRBL order (clockwise)
    def __init__(
        self, name, description, is_light,
        n_to=None, e_to=None, s_to=None, w_to=None
    ):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = []
        self.monsters = []

    def __getattr__(self, attr):
        return None

    def show_overview(self, has_light):
        if (self.is_light or has_light):
            print(f"\nLocation: {self.name}\n\n{self.description}\n")
            if len(self.monsters) != 0:
                print(
                    "You assess the room and recognize some monsters from "
                    "your bestiary:"
                )
                for monster in self.monsters:
                    print(f'    - {monster.name}')
                print()
            if len(self.items) != 0:
                print(f'You look around and see some items in the area:')
                for item in self.items:
                    print(f'    - {item.name} ({item.description})')
                print()
        else:
            print("\nIt's pitch black!\n")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, target):
        for i in range(len(self.items)):
            if self.items[i].name == target.name:
                del self.items[i]
                return

    def add_monster(self, monster):
        monster.room = self
        self.monsters.append(monster)

    def remove_monster(self, target):
        for i in range(len(self.monsters)):
            if self.monsters[i].name == target.name:
                print(f"You have vanquished {target.name}!\n")
                del self.monsters[i]
                return
        print(
            f'Error: Could not delete non-existent monster "{target.name}""'
            f'in room "{self.name}."\n'
        )
