"""

    This class is the generic console interface between player & program

"""
import RobotCleanerGame as rCG
import string


class Interface:
    def __init__(self, game: rCG.Game):
        self.game = game

    def show_current_state(self):
        if self.game.grid:
            print(self.game.grid)
        else:
            print(f"Grid not initialised")

        if self.game.robot:
            if self.game.robot.stack:
                print(f"Stack > ", end="")
                for index, item in enumerate(self.game.robot.stack):
                    if index == len(self.game.robot.stack) - 1:
                        end = "\n"
                    else:
                        end = ", "
                    print(f"{item}", end=end)
            else:
                print(f"Stack > empty")
            print("")
        else:
            print(f"Robot not initialised")

    @staticmethod
    def request_input(prompt: str, validation_values=None, convert_to_int=True, convert_to_lowercase=True):
        if validation_values is None:
            validation_values = []

        while True:

            try:
                received = input(prompt)

                if convert_to_int and received in string.digits:
                    received = int(received)
                elif convert_to_lowercase and not (received in string.digits):
                    received = received.lower()

                if received in validation_values or not validation_values:
                    return received
                else:
                    print("Value not accepted, please try again.\n")
            except ValueError:
                print("Value error, please try again.\n")

    def action_list_feedback(self) -> rCG.Action:
        lookup = {}

        print(f"Please select an action:")
        for count, a in enumerate(self.game.get_possible_actions()):
            disp_count = count + 1
            print(f"{disp_count} : ", end="")
            match a.__class__.__name__:
                case rCG.Drop.__name__:
                    print(f"drop to {a.coords}")
                case rCG.Move.__name__:
                    print(f"move to {a.coords}")
                case rCG.PickUp.__name__:
                    print(f"pick-up from {a.coords}")
                case rCG.Sweep.__name__:
                    print(f"sweep {a.coords}")
                case _:
                    raise ValueError(f"Interface.action_list_feedback: {a.__class__.__name__} not matched")

            lookup[disp_count] = a

        # Refresh command
        print(f"R : Refresh")
        lookup["r"] = rCG.Refresh()

        # Quit command
        print(f"Q : Quit")
        lookup["q"] = rCG.Quit()

        selected = self.request_input("\nSelect action: ", validation_values=list(lookup.keys()))

        return lookup[selected]

    def process_action(self, action) -> bool:
        # Boolean return determines whether the action is a stopper or not; False = stop
        self.game.history.append(action)
        match action.__class__.__name__:
            case rCG.Drop.__name__:
                if not self.game.apply_drop(action):
                    print("Drop failed!")
            case rCG.Move.__name__:
                self.game.apply_move(action)
            case rCG.PickUp.__name__:
                self.game.apply_pickup(action)
            case rCG.Refresh.__name__:
                self.show_current_state()
            case rCG.Sweep.__name__:
                self.game.apply_sweep(action)
            case rCG.Quit.__name__:
                return False  # Don't continue
            case _:
                raise ValueError(f"Interface.process_action: {action.__class__.__name__} not matched")

        # Continue by default
        return True


if __name__ == "__main__":
    pass
