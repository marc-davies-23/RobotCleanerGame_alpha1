"""

    Here we define tokens & token types:

    r, g, b: items that need to be tidied away
    R, G, B, *: bin receptacle for items of appropriate type; * accepts all
    m : mess to be swept up

    A token can only contain one of these.

    Properties of tokens:
     - if an item, can be picked up or dropped
     - if a receptacle, can accept an item of appropriate type
     - if a mess, can be swept

"""

ROBOT_TOKEN = "¥"

# Tokens short reference & description
TOKEN_DESCRIPTIONS: dict[str, str] = {
    ROBOT_TOKEN: "Robot",
    "r": "Food Item",
    "g": "Plastic Item",
    "b": "Glass Item",
    "R": "Food Bin",
    "G": "Plastic Bin",
    "B": "Glass Bin",
    "*": "Universal Bin",
    "m": "Mess",
}

SET_OF_ITEMS = {"r", "g", "b"}

SET_OF_BINS = {"R", "G", "B", "*"}

SET_OF_MESS = {"m"}

ITEMS_TO_BIN_MAP = {
    # Item : Bins which accept that item
    "r": {"R", "*"},
    "g": {"G", "*"},
    "b": {"B", "*"},
}

"""
## Not used yet, maybe later
class TokenProperties:
    can_pick = False
    can_sweep = False
    is_bin = False
    is_player = False


class TokenItem(TokenProperties):
    can_pick = True


class TokenBin(TokenProperties):
    is_bin = True


class TokenMess(TokenProperties):
    can_sweep = True


class TokenRobot(TokenProperties):
    is_player = True


TOKEN_PROPERTIES: dict[str, TokenProperties] = {
    "r": TokenItem(),
    "g": TokenItem(),
    "b": TokenItem(),
    "R": TokenBin(),
    "G": TokenBin(),
    "B": TokenBin(),
    "*": TokenBin(),
    "m": TokenMess(),
    ROBOT_TOKEN: TokenRobot(),
}
"""

if __name__ == "__main__":
    pass
