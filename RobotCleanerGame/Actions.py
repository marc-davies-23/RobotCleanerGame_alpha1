"""
    Actions here mean user input actions. The Action class itself is in effect an abstract class.

    Other classes inherit Action to define program controls.
"""


MOVE_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Action:
    pass


class Drop(Action):
    def __init__(self, coords: (int, int)):
        self.coords = coords


class Move(Action):
    def __init__(self, coords: (int, int)):
        self.coords = coords


class PickUp(Action):
    def __init__(self, coords: (int, int)):
        self.coords = coords


class Quit(Action):
    pass


class Refresh(Action):
    pass


class Sweep(Action):
    def __init__(self, coords: (int, int)):
        self.coords = coords


if __name__ == "__main__":
    pass
