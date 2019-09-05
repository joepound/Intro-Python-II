class Player:
    def __init__(self, name, current_room=None):
        self.name = name
        self.current_room = current_room
        self.items = []

    def add_item(self, item):
        self.items.append(item)
