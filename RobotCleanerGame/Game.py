"""

    Class for the main game functions, loop & processing actions.

    Game.grid: object of the Grid class
    Game.robot: object of the Robot class

"""
import RobotCleanerGame as rCG


class Game:
    def __init__(self, size_x: int, size_y: int, robot_start=None, interface=None, history=None):
        self.grid = None
        self.robot = None
        self.initialise_grid(size_x, size_y, robot_start)

        if interface is None:
            self.interface = rCG.Interface(game=self)
        else:
            self.interface = interface

        if history is None:
            self.history = []
        else:
            self.history = history

    def initialise_grid(self, size_x: int, size_y: int, robot_start=None):
        # Separate method so that games may be re-initialised
        self.grid = rCG.Grid(size_x, size_y)
        self.robot = rCG.Robot(start=robot_start)

        self.grid.set_tile(self.robot.coords, rCG.ROBOT_TOKEN)

    def add_token(self, coords: (int, int), token_symbol):
        if not (token_symbol in rCG.SET_OF_ITEMS | rCG.SET_OF_BINS | rCG.SET_OF_MESS):
            raise ValueError(f"Game.add_token: token_symbol not valid")

        if not self.grid.get_tile(coords).is_empty():
            raise ValueError(f"Game.add_token: tile at co-ordinates {coords} is not empty")

        self.grid.set_tile(coords, token_symbol)

    def get_possible_actions(self):
        actions = []

        for coord in self.grid.get_adjacent_coordinates(self.robot.coords):

            tile = self.grid.get_tile(coord)

            if tile.is_empty():
                # Can move or drop into an empty co-ord
                actions.append(rCG.Move(coord))
                if not self.robot.is_stack_empty():
                    actions.append(rCG.Drop(coord))
            elif tile.is_bin():
                # Can -- potentially -- drop an item into a bin
                if not self.robot.is_stack_empty():
                    actions.append(rCG.Drop(coord))
            elif tile.is_item():
                # Can pick up an item
                actions.append(rCG.PickUp(coord))
            elif tile.is_mess():
                actions.append(rCG.Sweep(coord))

        return actions

    def apply_drop(self, drop: rCG.Drop) -> bool:
        # Boolean return indicates whether item successfully dropped or not
        # First, pop the item; if we find nothing, exit
        if not (item := self.robot.drop()):
            return False

        # Can drop into empty tiles or bins; bins are more complicated. Deal with empty tile first
        tile = self.grid.get_tile(drop.coords)

        if tile.is_empty():
            self.grid.set_tile(drop.coords, item)
            return True

        # If we get to here we're dealing with bin tiles
        if tile.content() in rCG.ITEMS_TO_BIN_MAP[item]:
            # Accepted bin; we don't need to set the item here, it is "destroyed"
            return True
        else:
            # The robot can't drop the item otherwise so the robot has to pick it up again
            self.robot.pickup(item)
            return False

    def apply_move(self, move: rCG.Move):
        self.grid.get_tile(self.robot.coords).clear()

        self.grid.set_tile(move.coords, rCG.ROBOT_TOKEN)
        self.robot.coords = move.coords

    def apply_pickup(self, pickup: rCG.PickUp):
        tile = self.grid.get_tile(pickup.coords)
        if not tile.is_item():
            raise ValueError("Game.apply_pickup: wrong token type")

        if self.robot.pickup(tile.content()):
            tile.clear()

    def apply_sweep(self, sweep: rCG.Sweep):
        tile = self.grid.get_tile(sweep.coords)
        if tile.is_mess():
            tile.clear()

    def is_grid_cleared(self) -> bool:
        # Check the robot's not carrying anything first, this is fast to check; if he is, the grid isn't cleared
        if not self.robot.is_stack_empty():
            return False

        # Now check the grid; this is slower
        for j in self.grid.grid:
            for i in j:
                if not (i.content() in {rCG.EMPTY_TILE, rCG.ROBOT_TOKEN} | rCG.SET_OF_BINS):
                    return False

        # If we get here then the grid is cleared
        return True

    def start_control_loop(self):
        if self.interface is None:
            raise Exception("Game.start_control_loop: No Interface set")

        go = True

        while go:
            self.interface.show_current_state()

            action = self.interface.action_list_feedback()

            go = self.interface.process_action(action)

            if self.is_grid_cleared():
                print(f"Game Over!")


if __name__ == "__main__":
    pass
