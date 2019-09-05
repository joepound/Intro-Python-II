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

    def add_item(self, item):
        self.items.append(item)
