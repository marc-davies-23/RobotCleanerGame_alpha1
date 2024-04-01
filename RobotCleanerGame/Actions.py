MOVE_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Action:
    pass


class Drop(Action):
    def __init__(self, location: (int, int)):
        self.location = location


class Move(Action):
    def __init__(self, location: (int, int)):
        self.location = location


class PickUp(Action):
    def __init__(self, location: (int, int)):
        self.location = location


class Quit(Action):
    pass


class Refresh(Action):
    pass


class Sweep(Action):
    def __init__(self, location: (int, int)):
        self.location = location


if __name__ == "__main__":
    pass
    """
    m = Move((0, 1))

    print(m.__class__.__name__)
    """
