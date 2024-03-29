"""

    This class is the generic console interface between player & program

"""
import RobotCleanerGame


class Interface:
    def __init__(self, game: RobotCleanerGame.Game):
        self.game = game

    def get_action_list(self):
        actions = {"moves": self.game.get_available_move_coordinates()}

        return actions

    def get_game_state(self):
        return self.game

    """ don't like this at all, prefer action list concept
    @staticmethod
    def request_input(prompt: str, validation_values=None, convert_to_lowercase=True):
        if validation_values is None:
            validation_values = []

        while True:
            received = input(prompt)

            if convert_to_lowercase:
                received = received.lower()

            if not validation_values or received in validation_values:
                return received
            else:
                print("Value not accepted, please try again.\n")

    def request_move(self):
        prompt = "MOVE: enter "
        validation_list = []
        available_moves = self.game.get_available_moves()
        for move in available_moves:
            validation_list.append(move_map[move])
            prompt = prompt + move_text_map[move]

        return move_map_inv[self.request_input(prompt, validation_list)]"""


if __name__ == "__main__":
    pass
