import RobotCleanerGame as rCG

if __name__ == "__main__":
    g = rCG.Game(3, 3, robot_start=(2, 1))

    g.add_token((0, 0), "*")  # Universal bin

    g.add_token((1, 1), "b")  # Blue item
    g.add_token((2, 2), "r")  # Red item
    g.add_token((2, 0), "m")  # Mess

    g.start_control_loop()
