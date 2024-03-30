"""

    Here we define tokens & token types:

    r, g, b: items that need to be tidied away
    R, G, B, *: receptacle for items of appropriate type; * accepts all
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
    "r": "Red Item",
    "g": "Green Item",
    "b": "Blue Item",
    "R": "Red Bin",
    "G": "Green Bin",
    "B": "Blue Bin",
    "*": "Universal Bin",
    "m": "Mess",
    ROBOT_TOKEN: "Robot",
}


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

ITEMS = ["r", "g", "b"]

ITEMS_TO_BIN_MAP = {
    # Item : Bins which accept that item
    "r": ["R", "*"],
    "g": ["G", "*"],
    "b": ["B", "*"],
}

if __name__ == "__main__":
    pass
