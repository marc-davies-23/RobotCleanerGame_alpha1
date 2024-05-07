from BuildGameFromFile import *
from InterfacePyGame import *

if __name__ == "__main__":
    g = build_game_from_file("../GameFiles/SetPieces/Game1/game.rcgg")

    g.interface = InterfacePyGame(g)

    pygc = InterfacePyGame(g)

    pygc.execute()
