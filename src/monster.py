class Monster:
    def __init__(self, name, hp, description=None, room=None):
        self.name = name
        self.hp = hp
        self.description = description
        self.room = room

    def __getattr__(self, attr):
        return None

    def __str__(self):
        return (
            f"name: {self.name} | hp: {self.hp} | "
            f"description: {self.description} | room: {self.room}"
        )

    def __repr__(self):
        return (
            f"{type(self).__name__}({repr(self.name)}, {repr(self.hp)}, "
            f"{repr(self.description)}, {repr(self.room)})"
        )

    def on_attack(self, dmg, is_one_hit_kill):
        if is_one_hit_kill:
            self.hp = 0
            print(
                f'\nGodly power instantly struck down monster "{self.name}"!\n'
            )
            self.room.remove_monster(self)
        else:
            self.hp -= dmg
            print(f'Monster "{self.name}" took {dmg} damage.\n')
            if self.hp <= 0:
                self.room.remove_monster(self)
