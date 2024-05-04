from BuildGameFromFile import *
from InterfaceFromFile import *

if __name__ == "__main__":
    g = build_game_from_file("../GameFiles/SetPieces/Game1/game.rcgg")

    g.interface = InterfaceFromFile(g, "../GameFiles/SetPieces/Game1/solve.rcgs")

    g.start_control_loop()
