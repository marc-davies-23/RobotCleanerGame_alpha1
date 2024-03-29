MOVE_LIST = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Action:
    location: (int, int)


class Move(Action):
    def __init__(self, location: (int, int)):
        self.location = location


if __name__ == "__main__":
    pass
    """
    m = Move((0, 1))

    print(m.__class__.__name__)
    """
