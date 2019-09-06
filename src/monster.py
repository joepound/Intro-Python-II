class Monster:
    def __init__(self, name, hp, description=None):
        self.name = name
        self.hp = hp
        self.description = description

    def __getattr__(self, attr):
        return None
