import pygame

from game.board import Board
from game.player import Player
from ui.board_view import BoardView
from utils.constants import WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH


class ChessGame:
    """Main controller for the chess game."""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        # Game state
        self.board = Board()

        self.white_player = Player(
            name="White",
            color="white"
        )

        self.black_player = Player(
            name="Black",
            color="black"
        )

        self.current_player = self.white_player

        # Board user interface
        self.board_view = BoardView(self.screen)

        self.running = True

    def run(self) -> None:
        """Start and maintain the main game loop."""

        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            # Limit the game to 60 frames per second.
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self) -> None:
        """Handle keyboard, mouse, and window events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.handle_keyboard(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse(event)

    def handle_keyboard(self, event: pygame.event.Event) -> None:
        """Handle keyboard input."""

        if event.key == pygame.K_ESCAPE:
            self.running = False

    def handle_mouse(self, event: pygame.event.Event) -> None:
        """Handle mouse input.

        Chess piece selection and movement will be implemented here.
        """

        if event.button == 1:
            mouse_x, mouse_y = event.pos

            print(
                f"Mouse clicked at: "
                f"({mouse_x}, {mouse_y})"
            )

    def update(self) -> None:
        """Update the game state."""

        # Chess rules and movement logic
        # will be implemented here.
        pass

    def draw(self) -> None:
        """Draw everything on the screen."""

        self.screen.fill((30, 30, 30))

        # Draw chess board and pieces.
        self.board_view.draw(self.board)

        pygame.display.flip()
