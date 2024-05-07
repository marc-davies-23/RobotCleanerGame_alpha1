"""
    Interface incorporating PyGame functionality
"""
import pygame

from Game import Game
from Interface import Interface

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

DELAY_ONE_SEC = 1000
DELAY_REGULAR = 500

FILE_TILE = "TILE_64x64.png"

FILES_ROBOT = ["ROBOT_64x64L.png", "ROBOT_64x64R.png"]

FILES_BLUE_BIN = ["BLUE_BIN_64x64.png"]
FILES_GREEN_BIN = ["GREEN_BIN_64x64.png"]
FILES_RED_BIN = ["RED_BIN_64x64.png"]
FILES_UNIVERSAL_BIN = ["UNIVERSAL_BIN_64x64.png"]

FILES_BLUE_ITEM = ["BLUE_ITEM_64x64L.png", "BLUE_ITEM_64x64R.png"]
FILES_GREEN_ITEM = ["GREEN_ITEM_64x64L.png", "GREEN_ITEM_64x64R.png"]
FILES_RED_ITEM = ["RED_ITEM_64x64L.png", "RED_ITEM_64x64R.png"]

FILES_MESS = ["MESS_64x64L.png", "MESS_64x64R"]

FONT_COURIER_NEW = "couriernew"

PATH_TOKENS_BIG = "../GameFiles/Assets/Images/Tokens_Original/"
PATH_TOKENS_64 = "../GameFiles/Assets/Images/Tokens_Play/"

TILE_SIZE = 64

TITLE_STRING = "RobotCleanerGame v.0.0.a"

WIN_WIDTH = 800
WIN_HEIGHT = 600
WIN_CAPTION = "RobotCleanerGame"


class InterfacePyGame(Interface):
    pass


class PyGameControls:
    def __init__(self, game: Game, win_width: int = WIN_WIDTH, win_height: int = WIN_HEIGHT) -> None:
        self.game = game
        self.win_width = win_width
        self.win_height = win_height

        pygame.init()
        pygame.display.set_caption(WIN_CAPTION)

        self.window = pygame.display.set_mode((win_width, win_height))

        # Background tile
        self.tile_img = pygame.image.load(PATH_TOKENS_64 + FILE_TILE)

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
        self.window.blit(self.tile_img, (x, y))

    def execute(self) -> None:

        self.title_screen()

        run = True

        robot_token = PyGameToken(PATH_TOKENS_64, FILES_ROBOT)

        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            key = pygame.key.get_pressed()

            self.draw_background_tile(200, 200)
            robot_token.draw(self.window, 200, 200)

            pygame.display.update()

            pygame.time.delay(DELAY_REGULAR)
            self.window.fill(COLOR_BLACK)

        pygame.quit()


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


if __name__ == "__main__":
    """pygc = PyGameControls()
    pygc.execute()"""
    pass
