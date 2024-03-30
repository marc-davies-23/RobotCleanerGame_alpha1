import RobotCleanerGame

if __name__ == "__main__":
    g = RobotCleanerGame.Game()
    g.initialise_grid(3, 3, (2, 2))
    g.start_control_loop()