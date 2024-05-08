"""

    This Interface accepts a file instead of user input: for automation and test scripts

"""
from Actions import *
from BuildGameFromFile import *
from Interface import *


class InterfaceFromFile(Interface):
    def __init__(self, game, file_path) -> None:
        super().__init__(game)
        self.__actionList: [Action] = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.replace("\r", "").replace("\n", "")  # Strip out line breaks
                split = line.split("(")

                # Try to read the second part of the split; if out of index range, then there are no coords
                try:
                    coords = self.get_coords_from_str(split[1])

                except IndexError:
                    coords = None

                # Dynamically create action object
                self.__actionList.append(type(split[0], (object,), {"coords": coords})())

    @staticmethod
    def get_coords_from_str(input_string) -> (int, int):
        cds = input_string.replace(")", "").split(",")
        return int(cds[0]), int(cds[1])

    def listen_for_action(self) -> Action:
        # Simply return the front item from the action list; if the list is empty, print warning and Quit
        try:
            return self.__actionList.pop(0)
        except IndexError:
            print("Warning: end of Action list from file; Quitting")
            return Quit()


if __name__ == "__main__":
    g = build_game_from_file("../GameFiles/SetPieces/Game1/game.rcgg")
    i = InterfaceFromFile(g, "../GameFiles/SetPieces/Game1/solve.rcgs")
