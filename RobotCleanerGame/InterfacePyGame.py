"""
    Interface incorporating PyGame functionality
"""
import pygame

from Game import *
from Interface import Interface
from Robot import MAX_CARRY
from RobotCleanerGame import Action

BUTTON_WIDTH = 128

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

DELAY_ONE_SEC = 1000
DELAY_REGULAR = 50

FILE_TILE = "TILE_64x64.png"

FILES_ROBOT = ["ROBOT_64x64L.png", "ROBOT_64x64R.png"]

FILES_BLUE_BIN = ["BLUE_BIN_64x64.png"]
FILES_GREEN_BIN = ["GREEN_BIN_64x64.png"]
FILES_RED_BIN = ["RED_BIN_64x64.png"]
FILES_UNIVERSAL_BIN = ["UNIVERSAL_BIN_64x64.png"]

FILES_BLUE_ITEM = ["BLUE_ITEM_64x64L.png", "BLUE_ITEM_64x64R.png"]
FILES_GREEN_ITEM = ["GREEN_ITEM_64x64L.png", "GREEN_ITEM_64x64R.png"]
FILES_RED_ITEM = ["RED_ITEM_64x64L.png", "RED_ITEM_64x64R.png"]

FILES_MESS = ["MESS_64x64L.png", "MESS_64x64R.png"]

FONT_COURIER_NEW = "couriernew"

PATH_TOKENS_BIG = "../GameFiles/Assets/Images/Tokens_Original/"
PATH_TOKENS_64 = "../GameFiles/Assets/Images/Tokens_Play/"

TILE_IMG = pygame.image.load(PATH_TOKENS_64 + FILE_TILE)
TILE_SIZE = 64

TITLE_STRING = "RobotCleanerGame v.0.0.a"

FEEDBACK_TEXT_BOX_HEIGHT = 20
WIN_WIDTH = TILE_SIZE * 12
WIN_HEIGHT = TILE_SIZE * 11 + FEEDBACK_TEXT_BOX_HEIGHT  # 20 extra pixels for feedback text
WIN_CAPTION = "RobotCleanerGame"

B_DROP_P = pygame.image.load(PATH_TOKENS_64 + "B_DROP_PRESSED.png")
B_DROP_U = pygame.image.load(PATH_TOKENS_64 + "B_DROP_UNPRESSED.png")
B_MOVE_P = pygame.image.load(PATH_TOKENS_64 + "B_MOVE_PRESSED.png")
B_MOVE_U = pygame.image.load(PATH_TOKENS_64 + "B_MOVE_UNPRESSED.png")
B_PICK_P = pygame.image.load(PATH_TOKENS_64 + "B_PICKUP_PRESSED.png")
B_PICK_U = pygame.image.load(PATH_TOKENS_64 + "B_PICKUP_UNPRESSED.png")
B_SWEP_P = pygame.image.load(PATH_TOKENS_64 + "B_SWEEP_PRESSED.png")
B_SWEP_U = pygame.image.load(PATH_TOKENS_64 + "B_SWEEP_UNPRESSED.png")
B_UNAVAL = pygame.image.load(PATH_TOKENS_64 + "BUTTON_UNAVAILABLE.png")

STATE_FLAG_MOVE_PRESSED = Move.__name__
STATE_FLAG_DROP_PRESSED = Drop.__name__
STATE_FLAG_PICK_PRESSED = PickUp.__name__
STATE_FLAG_SWEP_PRESSED = Sweep.__name__

PRESSED_BUTTON = "pressed_button"

CURRENT_SCREEN = "current_screen"
MAIN_SCREEN = "main_screen"

FEEDBACK_MSG_PRESS_BUTTON = "Press a button to choose an action to perform."
FEEDBACK_MSG_CLICK_GRID = "Now click the grid to choose a tile to perform the action upon."
FEEDBACK_MSG_PERFORMED_ACTION = "Performed action: "
FEEDBACK_MSG_WRONG_TILE_FOR_ACTION = "Action can't be done here."
FEEDBACK_MSG_GRID_CLEARED = "All cleared!"

def map_pixel_to_tile_coord(pixel_coord: int) -> int:
    return int(pixel_coord / TILE_SIZE)


class InterfacePyGame(Interface):
    def __init__(self, game: Game, win_width: int = WIN_WIDTH, win_height: int = WIN_HEIGHT) -> None:
        super().__init__(game)
        self.state = {CURRENT_SCREEN: MAIN_SCREEN,
                      PRESSED_BUTTON: None}
        self.win_width = win_width
        self.win_height = win_height

        pygame.init()
        pygame.display.set_caption(WIN_CAPTION)

        self.window = pygame.display.set_mode((win_width, win_height))

        self.animation_beat = 0

        # Store for list of possible actions
        self.actions = []

        # Dictionary to store items on the screen that can be clicked
        self.screen_inventory = {}

        # Store feedback message
        self.feedback_msg = FEEDBACK_MSG_PRESS_BUTTON

    def give_user_feedback(self, feedback: str) -> None:
        self.feedback_msg = feedback

    def title_screen(self, title_size=32, color=COLOR_WHITE, x=200, y=100) -> None:
        self.window.fill(COLOR_BLACK)

        font = pygame.font.SysFont(FONT_COURIER_NEW, title_size, True)
        text = font.render(TITLE_STRING, True, color)
        self.window.blit(text, (x, y))

        robot256 = pygame.image.load(PATH_TOKENS_BIG + "ROBOT_256x256.png")
        robot_x = int(self.win_width / 2) - 128
        robot_y = y + 20
        self.window.blit(robot256, (robot_x, robot_y))

        pygame.display.update()
        pygame.time.delay(2 * DELAY_ONE_SEC)
        self.window.fill(COLOR_BLACK)

    def draw_background_tile(self, x: int, y: int) -> None:
        self.window.blit(TILE_IMG, (x, y))

    def draw_main_screen(self):
        # Clear the window first
        self.window.fill(COLOR_BLACK)

        # Buttons of Menu
        self.draw_menu()

        # Draw robot's stack
        self.draw_stack()

        ordered_actions = Game.order_actions_by_coords(self.actions)

        for y in range(0, self.game.grid.size_y):
            for x in range(0, self.game.grid.size_x):

                tile = self.game.grid.get_tile((x, y))
                self.draw_background_tile(x * TILE_SIZE, y * TILE_SIZE)

                if (x, y) in ordered_actions:
                    # Add the actions tied to this tile to the screen inventory
                    self.screen_inventory[(x, y)] = ordered_actions[(x, y)]

                if tile.is_empty():
                    # Go to next
                    continue

                TOKEN_MAP[tile.get_content()].draw(self.window, x * TILE_SIZE, y * TILE_SIZE, increment=self.beat())

    def draw_menu(self):
        # Draw the menu at the bottom left row
        x = 0
        y = self.win_height - TILE_SIZE - FEEDBACK_TEXT_BOX_HEIGHT

        avail = Game.is_action_type_in_actions(Move, self.actions)
        self.draw_menu_button(Move, avail, STATE_FLAG_MOVE_PRESSED, B_MOVE_P, B_MOVE_U, x, y)

        x += BUTTON_WIDTH
        avail = Game.is_action_type_in_actions(PickUp, self.actions)
        self.draw_menu_button(PickUp, avail, STATE_FLAG_PICK_PRESSED, B_PICK_P, B_PICK_U, x, y)

        x += BUTTON_WIDTH
        avail = Game.is_action_type_in_actions(Drop, self.actions)
        self.draw_menu_button(Drop, avail, STATE_FLAG_DROP_PRESSED, B_DROP_P, B_DROP_U, x, y)

        x += BUTTON_WIDTH
        avail = Game.is_action_type_in_actions(Sweep, self.actions)
        self.draw_menu_button(Sweep, avail, STATE_FLAG_SWEP_PRESSED, B_SWEP_P, B_SWEP_U, x, y)

        if len(self.feedback_msg) > 0:
            self.feedback_box()

    def draw_menu_button(self, action, available, state_flag, image_pressed, image_unpressed, x, y) -> None:
        if not available:
            image = B_UNAVAL
        elif self.state[PRESSED_BUTTON] == state_flag:
            image = image_pressed
        else:
            image = image_unpressed

            # Add the button to the screen inventory with Tile coords; other it is inactive
            tile_x, tile_y = map_pixel_to_tile_coord(x), map_pixel_to_tile_coord(y)

            # The buttons are two tiles wide, so add two indices
            self.screen_inventory[(tile_x, tile_y)] = action
            self.screen_inventory[(tile_x + 1, tile_y)] = action

        self.window.blit(image, (x, y))

    def feedback_box(self, font_size=16, color=COLOR_WHITE):
        x = 16
        y = WIN_HEIGHT - FEEDBACK_TEXT_BOX_HEIGHT + 2

        font = pygame.font.SysFont(FONT_COURIER_NEW, font_size, True)
        text = font.render(self.feedback_msg, True, color)
        self.window.blit(text, (x, y))

    def draw_stack(self):
        marker_image = pygame.image.load(PATH_TOKENS_64 + "CARRIED_ITEMS_MARKER_64x64.png")

        # Draw it one tile to the right of the game grid
        x = self.game.grid.size_x * TILE_SIZE

        # Draw it from the bottom, but leave space for a stack as well as icon underneath
        y = max(self.game.grid.size_y, MAX_CARRY) * TILE_SIZE

        # Base
        self.window.blit(marker_image, (x, y))

        for item in self.game.robot.stack:
            y -= TILE_SIZE
            TOKEN_MAP[item].draw(self.window, x, y, False)

    def event_start(self) -> None:
        self.title_screen()

    def event_begin_of_loop(self) -> None:
        pygame.time.delay(DELAY_REGULAR)

        # Default animation beats are hit once every ten loops
        self.animation_beat = (self.animation_beat + 1) % 10

        # Get possible actions
        self.actions = self.game.get_possible_actions()

        # Refresh the screen inventory
        self.screen_inventory = {}

    def event_grid_cleared(self) -> None:
        self.give_user_feedback(FEEDBACK_MSG_GRID_CLEARED)

    def event_quit(self) -> None:
        pygame.quit()

    def beat(self) -> bool:
        # Are we on an animation beat?
        return self.animation_beat == 0

    def display_state(self) -> None:

        if True:
            # Draw principle screen
            self.draw_main_screen()

        pygame.display.update()

    def listen_for_action(self) -> (Action | None):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return Quit()
                case pygame.MOUSEBUTTONUP:
                    return self.process_mouse_click()
                case _:
                    pass

        # key = pygame.key.get_pressed()

        return None

    def process_mouse_click(self) -> (Action | None):
        pos = pygame.mouse.get_pos()
        x = map_pixel_to_tile_coord(pos[0])
        y = map_pixel_to_tile_coord(pos[1])
        try:
            screen_item = self.screen_inventory[(x, y)]

        except KeyError:
            # Nothing in inventory, just quit
            return None

        try:
            # Try to set a pressed button state
            if screen_item.__name__ in {STATE_FLAG_MOVE_PRESSED, STATE_FLAG_DROP_PRESSED,
                                        STATE_FLAG_PICK_PRESSED, STATE_FLAG_SWEP_PRESSED}:
                self.state[PRESSED_BUTTON] = screen_item.__name__
                self.feedback_msg = FEEDBACK_MSG_CLICK_GRID
        except AttributeError:
            # If not applicable, continue
            pass

        # Catch no button pressed and stop here
        if self.state[PRESSED_BUTTON] is None:
            return None

        try:
            for a in screen_item:
                if a.__class__.__name__ == self.state[PRESSED_BUTTON]:
                    # Can reset the Pressed Button state
                    self.state[PRESSED_BUTTON] = None
                    self.feedback_msg = FEEDBACK_MSG_PERFORMED_ACTION + a.__class__.__name__
                    return a

                # If we found nothing...
                self.feedback_msg = FEEDBACK_MSG_WRONG_TILE_FOR_ACTION

        except TypeError:
            # Continue
            pass

        # Last catch all
        return None


class PyGameToken:
    def __init__(self, folder: str, files: [str]) -> None:
        self.anim_idx = 0
        self.anim_max = len(files) - 1

        if self.anim_max < 0:
            raise FileNotFoundError("PyGameToken.__init__: empty files list")

        self.images = []

        for file in files:
            self.images.append(pygame.image.load(folder + file))

    def get_current_image(self) -> pygame.Surface:
        return self.images[self.anim_idx]

    def increment_idx(self) -> None:
        if self.anim_max == 0:
            # If max is zero, there's only one image; don't bother incrementing index
            return

        if self.anim_idx == self.anim_max:
            # Start again
            self.anim_idx = 0
        else:
            self.anim_idx += 1

    def draw(self, window, x: int, y: int, increment: bool = True) -> None:
        window.blit(self.get_current_image(), (x, y))
        if increment:
            self.increment_idx()


TOKEN_MAP: dict[str, PyGameToken] = {
    "r": PyGameToken(PATH_TOKENS_64, FILES_RED_ITEM),
    "g": PyGameToken(PATH_TOKENS_64, FILES_GREEN_ITEM),
    "b": PyGameToken(PATH_TOKENS_64, FILES_BLUE_ITEM),
    "R": PyGameToken(PATH_TOKENS_64, FILES_RED_BIN),
    "G": PyGameToken(PATH_TOKENS_64, FILES_GREEN_BIN),
    "B": PyGameToken(PATH_TOKENS_64, FILES_BLUE_BIN),
    "*": PyGameToken(PATH_TOKENS_64, FILES_UNIVERSAL_BIN),
    "m": PyGameToken(PATH_TOKENS_64, FILES_MESS),
    ROBOT_TOKEN: PyGameToken(PATH_TOKENS_64, FILES_ROBOT),
}

if __name__ == "__main__":
    pass
