"""

    Class for the main game loop & controls

"""
import RobotCleanerGame


class Game:
    grid = None
    robot = None

    def initialise_grid(self, size_x: int, size_y: int, robot_start=None):
        self.grid = RobotCleanerGame.Grid(size_x, size_y)
        if robot_start is None:
            self.robot = RobotCleanerGame.Robot()
        else:
            self.robot = RobotCleanerGame.Robot(start=robot_start)

        self.grid.set_tile(self.robot.location, RobotCleanerGame.ROBOT_TOKEN)

    def get_available_move_coordinates(self):
        available_move_coords = []

        for coord in self.grid.get_adjacent_coordinates(self.robot.location):

            if self.grid.get_tile(coord).is_empty():
                available_move_coords.append(coord)

        return available_move_coords

    def apply_move(self, new_coords: (int, int)):
        self.robot.history.append(self.robot.location)
        self.grid.get_tile(self.robot.location).clear()

        self.grid.set_tile(new_coords, RobotCleanerGame.ROBOT_TOKEN)
        self.robot.location = new_coords


if __name__ == "__main__":
    pass
