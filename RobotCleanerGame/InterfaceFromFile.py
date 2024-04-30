"""

    This Interface accepts a file instead of user input: for automation and test scripts

"""

class InterfaceFromFile(Interface):
    def __init__(self, game, file_path) -> None:
        self.__super__(game)
        self.__file = []
        with open(file_path, "r") as file:
            pass


if __name__ == "__main__":
    pass