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
ITEM_TOKEN_TYPE = 1
BIN_TOKEN_TYPE = 2
MESS_TOKEN_TYPE = 3
ROBOT_TOKEN_TYPE = 4

ROBOT_TOKEN = "¥"

# Tokens short reference & description
token_descriptions: dict[str, str] = {
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
    type = 0


class TokenItem(TokenProperties):
    def __init__(self):
        self.type = ITEM_TOKEN_TYPE


class TokenBin(TokenProperties):
    def __init__(self):
        self.type = BIN_TOKEN_TYPE


class TokenMess(TokenProperties):
    def __init__(self):
        self.type = MESS_TOKEN_TYPE


class TokenRobot(TokenProperties):
    def __init__(self):
        self.type = ROBOT_TOKEN_TYPE


token_properties: dict[str, TokenProperties] = {
    "r": TokenItem(),
    "g": TokenItem(),
    "b": TokenItem(),
    "R": TokenBin(),
    "G": TokenBin(),
    "B": TokenBin(),
    "m": TokenMess(),
    ROBOT_TOKEN: TokenRobot(),
}

items = ["r", "g", "b"]

item_to_bin_map = {
    "r": ["R", "*"],
    "g": ["G", "*"],
    "b": ["B", "*"],
}

if __name__ == "__main__":
    pass
