"""

    Defines the classes for grid & tiles on which the game is played

"""
import RobotCleanerGame

EMPTY_TILE = "."


class Tile:
    def __init__(self):
        self.content = EMPTY_TILE

    def __str__(self):
        return self.content

    def is_empty(self):
        return self.content == EMPTY_TILE

    def fill(self, new_content):
        if self.is_empty():
            self.content = new_content
            return 1  # OK
        else:
            return 0  # Not OK

    def clear(self):
        self.content = EMPTY_TILE


class Grid:
    def __init__(self, x: int, y: int):
        self.grid = []
        self.size_x = x
        self.size_y = y
        for j in range(y):
            row = []
            for i in range(x):
                tile = Tile()
                row.append(tile)
            self.grid.append(row)

    def __str__(self):
        out = ""
        for j in self.grid:
            for i in j:
                out = out + i.content
            out = out + "\n"

        return out

    def get_tile(self, coordinates: (int, int)):
        return self.grid[coordinates[1]][coordinates[0]]

    def get_adjacent_coordinates(self, from_coord: (int, int)):
        adjacent_coordinates = []

        for move in RobotCleanerGame.move_list:
            x = from_coord[0] + move[0]
            if x < 0 or x >= self.size_x:
                continue
            y = from_coord[1] + move[1]
            if y < 0 or y >= self.size_y:
                continue
            adjacent_coordinates.append((x, y))

        return adjacent_coordinates

    def set_tile(self, coordinates: (int, int), new_content) -> None:
        self.grid[coordinates[1]][coordinates[0]].fill(new_content)


if __name__ == "__main__":
    pass
