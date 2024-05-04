"""
    Actions here mean user input actions that translate into robot/program functions.

    The Action class itself is in effect an abstract class. Other classes inherit Action to define robot/program
    controls.
"""

MOVE_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Action:
    """
        For now the base Action class is essentially an abstract class, and a placeholder for further functionality
        as necessary. The class is given coords of None here to signal that it is an action not reliant on the grid;
        some subclasses will overwrite this to make functional use of coords
    """

    def __init__(self) -> None:
        self.coords = None


class ActionWithCoords:
    """
        Second abstract class; this is an action with coords
    """
    def __init__(self, coords: (int, int)) -> None:
        self.coords = coords


class Drop(ActionWithCoords):
    """
        Action for the Robot to drop the top of its stack
    """
    pass


class Move(ActionWithCoords):
    """
        Action for the Robot to move to coords
    """
    pass


class PickUp(ActionWithCoords):
    """
        Action for Robot to try to pick up something from coords
    """
    pass


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


class Sweep(ActionWithCoords):
    """
        Action to Sweep something from board
    """
    pass


if __name__ == "__main__":
    pass
