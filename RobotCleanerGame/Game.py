"""

    Class for the main game loop & controls

"""
import RobotCleanerGame as rcg


class Game:
    grid: rcg.Grid
    robot: rcg.Robot
    interface: rcg.Interface
    history: list[rcg.Actions]

    def __init__(self, interface=None, history=None):
        if interface is None:
            self.interface = rcg.Interface(game=self)
        else:
            self.interface = interface

        if history is None:
            self.history = []
        else:
            self.history = history

    def initialise_grid(self, size_x: int, size_y: int, robot_start=None):
        self.grid = rcg.Grid(size_x, size_y)
        self.robot = rcg.Robot(start=robot_start)

        self.grid.set_tile(self.robot.location, rcg.ROBOT_TOKEN)

    def get_available_move_coordinates(self):
        available_move_coords = []

        for coord in self.grid.get_adjacent_coordinates(self.robot.location):

            if self.grid.get_tile(coord).is_empty():
                available_move_coords.append(coord)

        return available_move_coords

    def apply_move(self, move: rcg.Move):
        self.grid.get_tile(self.robot.location).clear()

        self.grid.set_tile(move.location, rcg.ROBOT_TOKEN)
        self.robot.location = move.location

    def start_control_loop(self):
        if self.interface is None:
            raise Exception("No Interface set")

        go = True

        while go:
            self.interface.show_current_state()

            action = self.interface.action_list_feedback()

            go = self.interface.process_action(action)


if __name__ == "__main__":
    pass
