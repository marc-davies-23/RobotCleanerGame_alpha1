"""

    Defines the classes for grid & tiles on which the game is played

"""

from Actions import MOVE_LIST
from Game import *
from Tokens import *

EMPTY_TILE = "."

DEFAULT_GRID_SIZE = 3


class Tile:
    def __init__(self) -> None:
        self.__content = EMPTY_TILE

    def __str__(self) -> str:
        return self.__content

    def is_bin(self) -> bool:
        return self.__content in SET_OF_BINS

    def is_empty(self) -> bool:
        return self.__content == EMPTY_TILE

    def is_item(self) -> bool:
        return self.__content in SET_OF_ITEMS

    def is_mess(self) -> bool:
        return self.__content in SET_OF_MESS

    def content(self) -> str:
        return self.__content

    def set(self, new_content) -> bool:
        if self.is_empty():
            self.__content = new_content
            return True  # OK
        else:
            return False  # Not OK

    def clear(self) -> None:
        self.__content = EMPTY_TILE


class Grid:
    def __init__(self, x: int = DEFAULT_GRID_SIZE, y: int = DEFAULT_GRID_SIZE) -> None:
        self.grid = []
        self.size_x = x
        self.size_y = y
        for j in range(y):
            row = []
            for i in range(x):
                tile = Tile()
                row.append(tile)
            self.grid.append(row)

    def __str__(self) -> str:
        out = ""
        for j in self.grid:
            for i in j:
                out = out + i.content()
            out = out + "\n"

        return out

    def get_tile(self, coordinates: (int, int)) -> Tile:
        return self.grid[coordinates[1]][coordinates[0]]

    def get_adjacent_coordinates(self, from_cds: (int, int)) -> [(int, int)]:
        adjacent_coordinates = []

        for move in MOVE_LIST:
            x = from_cds[0] + move[0]
            if x < 0 or x >= self.size_x:
                continue
            y = from_cds[1] + move[1]
            if y < 0 or y >= self.size_y:
                continue

            adjacent_coordinates.append((x, y))

        return adjacent_coordinates

    def set_tile(self, coordinates: (int, int), content) -> None:
        if not self.grid[coordinates[1]][coordinates[0]].set(content):
            raise ValueError(f"Grid.set_tile: could not set content")


if __name__ == "__main__":
    print(grid := Grid())
