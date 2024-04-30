"""

    A set of functions to build a game from a file

"""
from Game import Game


def read_file_to_buffer(file_path) -> [str]:
    buffer = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.replace("\r", "")
            buffer.append(line.replace("\n", ""))  # Strip out line breaks

    return buffer


def build_game_from_buffer(buffer: [str]) -> Game:
    """
        Breaks up the buffer into actionable parts.

        The first line of the buffer should consist of four numbers:
        sizeX (of grid), sizeY (of grid), X coords (of robot), Y coords (of robot)

        Each line onwards consists of a format like so:
        T(x,y)
        where T is a token type, and x, y are its coords.
    """
    line1 = buffer[0].split(",")

    if len(line1) != 4:
        raise IOError("build_game_from_buffer: first line of file translate to four values.")

    g = Game(int(line1[0]), int(line1[1]), robot_start=(int(line1[2]), int(line1[3])))

    for line in buffer[1:]:
        coords = line[1:].replace("(", "").replace(")", "").split(",")

        g.add_token((int(coords[0]), int(coords[1])), line[0])

    return g


def build_game_from_file(file_path) -> Game:
    buffer = read_file_to_buffer(file_path)
    return build_game_from_buffer(buffer)


if __name__ == "__main__":
    pass