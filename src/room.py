class Room:
    # Same order for adjacent rooms as HTML -> top-right-bottom-left (TRBL)
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
