import RobotCleanerGame

if __name__ == "__main__":
    iface = RobotCleanerGame.Interface(RobotCleanerGame.Game())
    iface.game.initialise_grid(3, 3, (2, 2))
    print(iface.game.grid)
    a = iface.action_list_feedback()
    iface.process_action(a)
    print(iface.game.grid)

