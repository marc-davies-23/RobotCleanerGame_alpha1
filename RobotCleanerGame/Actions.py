"""
    Actions here mean user input actions that translate into robot/program functions.

    The Action class itself is in effect an abstract class. Other classes inherit Action to define robot/program
    controls.
"""

MOVE_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Action:
    """
        For now the base Action class is essentially an abstract class, and a placeholder for further functionality
        as necessary.
    """
    pass


class Drop(Action):
    """
        Action for the Robot to drop the top of its stack
    """
    def __init__(self, coords: (int, int)) -> None:
        self.coords = coords


class Move(Action):
    """
        Action for the Robot to move to coords
    """
    def __init__(self, coords: (int, int)) -> None:
        self.coords = coords


class PickUp(Action):
    """
        Action for Robot to try to pick up something from coords
    """
    def __init__(self, coords: (int, int)) -> None:
        self.coords = coords


class Quit(Action):
    """
        Action to Quit current game
    """
    pass


class Refresh(Action):
    """
        Action to refresh display of game state
    """
    pass


class Sweep(Action):
    """
        Action to Sweep something from board
    """
    def __init__(self, coords: (int, int)) -> None:
        self.coords = coords


if __name__ == "__main__":
    pass
