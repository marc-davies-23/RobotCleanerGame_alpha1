"""
    Interface incorporating PyGame functionality
"""
import pygame

from Game import *
from Interface import Interface
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

WIN_WIDTH = TILE_SIZE * 12
WIN_HEIGHT = TILE_SIZE * 11
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


class InterfacePyGame(Interface):
    def __init__(self, game: Game, win_width: int = WIN_WIDTH, win_height: int = WIN_HEIGHT) -> None:
        super().__init__(game)
        self.state = {"pressed_button": None}
        self.win_width = win_width
        self.win_height = win_height

        pygame.init()
        pygame.display.set_caption(WIN_CAPTION)

        self.window = pygame.display.set_mode((win_width, win_height))

        self.animation_beat = 0

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

    def draw_menu(self):
        x = 0
        y = self.win_height - TILE_SIZE

        actions = self.game.get_possible_actions()

        avail = Game.is_action_type_in_actions(Move, actions)
        self.draw_menu_button(avail, "M", B_MOVE_P, B_MOVE_U, x, y)

        x += BUTTON_WIDTH
        avail = Game.is_action_type_in_actions(PickUp, actions)
        self.draw_menu_button(avail, "P", B_PICK_P, B_PICK_U, x, y)

        x += BUTTON_WIDTH
        avail = Game.is_action_type_in_actions(Drop, actions)
        self.draw_menu_button(avail, "D", B_DROP_P, B_DROP_U, x, y)

        x += BUTTON_WIDTH
        avail = Game.is_action_type_in_actions(Sweep, actions)
        self.draw_menu_button(avail, "S", B_SWEP_P, B_SWEP_U, x, y)

    def draw_menu_button(self, available, state_flag, image_pressed, image_unpressed, x, y) -> None:
        if not available:
            self.window.blit(B_UNAVAL, (x, y))
        elif self.state["pressed_button"] == state_flag:
            self.window.blit(image_pressed, (x, y))
        else:
            self.window.blit(image_unpressed, (x, y))

    def event_start(self) -> None:
        self.title_screen()

    def event_begin_of_loop(self) -> None:
        pygame.time.delay(DELAY_REGULAR)

    def event_quit(self) -> None:
        pygame.quit()

    def beat(self) -> bool:
        # Are we on an animation beat?
        return self.animation_beat == 0

    def display_state(self) -> None:
        # Default animation beats are hit once every ten loops
        self.animation_beat = (self.animation_beat + 1) % 10

        # Clear the window first
        self.window.fill(COLOR_BLACK)

        # Buttons of Menu
        self.draw_menu()

        for y in range(0, self.game.grid.size_y):
            for x in range(0, self.game.grid.size_x):

                tile = self.game.grid.get_tile((x, y))
                self.draw_background_tile(x * TILE_SIZE, y * TILE_SIZE)

                if tile.is_empty():
                    # Go to next
                    continue

                TOKEN_MAP[tile.get_content()].draw(self.window, x * TILE_SIZE, y * TILE_SIZE, increment=self.beat())

        pygame.display.update()

    def listen_for_action(self) -> (Action | None):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return Quit()
                case pygame.MOUSEBUTTONDOWN:
                    print(f"mouse start: {pygame.mouse.get_pos()}")
                case pygame.MOUSEBUTTONUP:
                    print(f"mouse end: {pygame.mouse.get_pos()}")
                case _:
                    pass

        # key = pygame.key.get_pressed()

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
    """pygc = PyGameControls()
    pygc.execute()"""
    pass
