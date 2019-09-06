class Monster:
    def __init__(self, name, hp, description=None, room=None):
        self.name = name
        self.hp = hp
        self.description = description
        self.room = room

    def __getattr__(self, attr):
        return None

    def on_attack(self, dmg):
        self.hp -= dmg
        print(f'Monster "{self.name}" took {dmg} damage.\n')
        if self.hp <= 0:
            self.room.remove_monster(self)
