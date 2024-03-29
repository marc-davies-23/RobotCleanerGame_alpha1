"""

    This class is the generic console interface between player & program

"""
import RobotCleanerGame


class Interface:
    def __init__(self, game: RobotCleanerGame.Game):
        self.game = game

    def get_possible_actions(self):
        actions = []
        # Moves first
        for c in self.game.get_available_move_coordinates():
            actions.append(RobotCleanerGame.Move(c))

        return actions

    @staticmethod
    def request_input(prompt: str, validation_values=None, convert_to_int=False, convert_to_lowercase=True):
        if validation_values is None:
            validation_values = []

        while True:
            received = input(prompt)

            if convert_to_int:
                received = int(received)

            if convert_to_lowercase:
                received = received.lower()

            if received in validation_values or not validation_values:
                return received
            else:
                print("Value not accepted, please try again.\n")

    def action_list_feedback(self):
        possible = self.get_possible_actions()

        lookup = {}
        count = 0

        print(f"Please select an action:")
        for a in possible:
            match a.__class__.__name__:
                case "Move":
                    print(f"{count} : move to {a.location}")
                case _:
                    print(f"{count} : unknown action")

            lookup[count] = a
            count = count + 1

        selected = self.request_input("\nSelect action: ", convert_to_int=True, convert_to_lowercase=False)

        return lookup[selected]

    def process_action(self, action):
        match action.__class__.__name__:
            case "Move":
                self.game.apply_move(action.location)
            case _:
                pass


if __name__ == "__main__":
    pass
