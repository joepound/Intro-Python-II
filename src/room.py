class Room:
    # Same directional order for adjacent rooms as CSS TRBL order (clockwise)
    def __init__(
        self, name, description,
        n_to=None, e_to=None, s_to=None, w_to=None
    ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = []

    def __getattr__(self, attr):
        return None

    def show_overview(self):
        print(f"\nLocation: {self.name}\n\n{self.description}\n")
        if len(self.items) != 0:
            print(f'You look around and see some items in the area:')
            for item in self.items:
                print(f'   - {item.name} ({item.description})')
            print()

    def add_item(self, item):
        self.items.append(item)
