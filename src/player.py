from lightsource import LightSource
from weapon import Weapon


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.has_light_source = False
        self.last_used = None

        #   ==================
        #   || CHEAT VALUES ||
        #   ==================

        self.is_helios = False

    def __getattr__(self, attr):
        return None

    def show_location(self):
        self.current_room.show_overview(
            self.has_light_source or self.is_helios
        )

    def move_to_room(self, room):
        if room is None:
            print("\nYou cannot move in that direction right now.\n")
        else:
            self.current_room = room
            self.current_room.show_overview(
                self.has_light_source or self.is_helios
            )

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
        if (self.current_room.is_light or self.has_light_source or
                self.is_helios):
            if len(self.current_room.monsters) == 0:
                for item in self.current_room.items:
                    if item.name == target:
                        is_grabbable, is_win_condition = item.on_take()
                        if is_grabbable:
                            if is_win_condition:
                                return (True, item.name)
                            if isinstance(item, LightSource):
                                self.has_light_source = True
                            self.items.append(item)
                            self.last_used = item
                            self.current_room.remove_item(item)
                            return (False, item.name)
                        return (False, None)
                print("\nNo such item in this room.\n")
                return (False, None)
            else:
                print(
                    "\nYou cannot grab an item with monsters around - you'll "
                    "be helpless!\n"
                )
                return (False, None)
        else:
            print("\nGood luck finding that in the dark!\n")
            return (False, None)

    def drop_item(self, target):
        if target == "it":
            if self.last_used is None:
                print("\nI don't know which item you mean.\n")
                return
            target = self.last_used.name
            self.last_used = None
        has_found_item = False
        has_dropped_light_source = False
        for i in range(len(self.items)):
            if self.items[i].name == target:
                self.items[i].on_drop()
                if isinstance(self.items[i], LightSource):
                    has_dropped_light_source = True
                self.current_room.add_item(self.items[i])
                del self.items[i]
                has_found_item = True
                break
        if not has_found_item:
            print("\nYou do not currently have any such item.\n")
        elif has_dropped_light_source:
            has_other_light_source = False
            for i in range(len(self.items)):
                if isinstance(self.items[i], LightSource):
                    has_other_light_source = True
                    break
            if not has_other_light_source:
                self.has_light_source = False

    def attack(self, target):
        if (self.current_room.is_light or self.has_light_source or
                self.is_helios):
            for monster in self.current_room.monsters:
                if monster.name == target:
                    weapon_used = input("\nAttack with what? ").lower().strip()
                    if weapon_used == "fists":
                        print("\nYou're not serious, are you?\n")
                    else:
                        if weapon_used == "it":
                            if self.last_used is None:
                                print("\nI don't know which weapon you mean.\n")
                                return
                            if not isinstance(self.last_used, Weapon):
                                print("\nThat item is not a weapon.\n")
                                return
                            weapon_used = self.last_used.name
                        for item in self.items:
                            if item.name == weapon_used:
                                if isinstance(item, Weapon):
                                    print(
                                        "\nYou attack with your {}!\n".format(
                                            weapon_used
                                        )
                                    )
                                    monster.on_attack(item.ap)
                                else:
                                    print("\nThat item is not a weapon.\n")
                                return
                        print("\nYou do not currently have any such weapon.\n")
                    return
            print("\nNo such monster in the current room.\n")
        else:
            print(
                "\nTry as you might, you are unable to attack accurately in "
                "the dark!\n"
            )

    #   ===================
    #   || CHEAT METHODS ||
    #   ===================

    def set_helios(self, flag):
        if flag == "1":
            self.is_helios = True
            print("\nHelios the sun god has blessed you with eternal light!\n")
            return True
        elif flag == "0":
            self.is_helios = False
            print("\nHelios has forsaken you.\n")
            return True
        return False

    def teleport(self, target, rooms):
        for room in rooms.values():
            if room.name.lower() == target:
                self.current_room = room
                print("\nWhat kind of compass are you using???\n")
                return True
        return False
