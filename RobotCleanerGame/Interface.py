"""

    This class is the generic console interface between player & program

"""

from Actions import *
from Game import *

import string


class Interface:
    def __init__(self, game) -> None:
        self.game = game

    def show_current_state(self) -> None:
        if self.game.grid:
            print(self.game.grid)
        else:
            print(f"Grid not initialised")

        if self.game.robot_img:
            if self.game.robot_img.stack:
                print(f"Stack > ", end="")
                max_idx = len(self.game.robot_img.stack) - 1
                for index, item in enumerate(self.game.robot_img.stack):
                    if index == max_idx:
                        end = "\n"
                    else:
                        end = ", "
                    print(f"{item}", end=end)
            else:
                print(f"Stack > empty")
            print("")
        else:
            print(f"Robot not initialised")

    def choose_action(self) -> Action:
        lookup = {}

        print(f"Please select an action:")
        for count, a in enumerate(self.game.get_possible_actions()):
            disp_count = count + 1
            print(f"{disp_count} : ", end="")
            match a.__class__.__name__:
                case Drop.__name__:
                    print(f"drop to {a.coords}")
                case Move.__name__:
                    print(f"move to {a.coords}")
                case PickUp.__name__:
                    print(f"pick-up from {a.coords}")
                case Sweep.__name__:
                    print(f"sweep {a.coords}")
                case _:
                    raise ValueError(f"Interface.action_list_feedback: {a.__class__.__name__} not matched")

            lookup[disp_count] = a

        # Refresh command
        print(f"R : Refresh")
        lookup["r"] = Refresh()

        # Quit command
        print(f"Q : Quit")
        lookup["q"] = Quit()

        selected = request_input("\nSelect action: ", validation_values=list(lookup.keys()))

        return lookup[selected]

    def process_action(self, action) -> bool:
        # Boolean return determines whether the action is a stopper or not; False = stop
        self.game.history.append(action)
        match action.__class__.__name__:
            case Drop.__name__:
                if not self.game.apply_drop(action):
                    print("Drop failed!")
            case Move.__name__:
                self.game.apply_move(action)
            case PickUp.__name__:
                self.game.apply_pickup(action)
            case Refresh.__name__:
                self.show_current_state()
            case Sweep.__name__:
                self.game.apply_sweep(action)
            case Quit.__name__:
                return False  # Don't continue
            case _:
                raise ValueError(f"Interface.process_action: {action.__class__.__name__} not matched")

        # Continue by default
        return True

    def event_grid_cleared(self) -> None:
        # This method isn't static as it may be used for more complex functionality later
        print(f"\nGRID CLEARED!\n")

    def event_quit(self) -> None:
        # This method isn't static as it may be used for more complex functionality later
        print(f"\nQuitting game.")


def request_input(prompt: str, validation_values=None, convert_to_int=True, convert_to_lowercase=True) -> str:
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


if __name__ == "__main__":
    pass
