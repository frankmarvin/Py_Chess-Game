import pygame

from game.board import Board
from utils.constants import (
    BOARD_SIZE,
    DARK_SQUARE,
    LIGHT_SQUARE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)


class BoardView:
    """Handles the visual display of the chess board."""

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        # Keep the board square on the screen.
        self.board_pixel_size = min(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        self.square_size = (
            self.board_pixel_size // BOARD_SIZE
        )

        # Fonts
        self.piece_font = pygame.font.SysFont(
            "dejavusans",
            56
        )

        self.coordinate_font = pygame.font.SysFont(
            "arial",
            16
        )

    def draw(self, board: Board) -> None:
        """Draw the complete chess board."""

        self.draw_squares()
        self.draw_coordinates()
        self.draw_pieces(board)

    def draw_squares(self) -> None:
        """Draw all 64 chess board squares."""

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                if (row + col) % 2 == 0:
                    square_color = LIGHT_SQUARE
                else:
                    square_color = DARK_SQUARE

                rectangle = pygame.Rect(
                    col * self.square_size,
                    row * self.square_size,
                    self.square_size,
                    self.square_size,
                )

                pygame.draw.rect(
                    self.screen,
                    square_color,
                    rectangle
                )

    def draw_coordinates(self) -> None:
        """Draw chess board coordinates."""

        files = "abcdefgh"

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                # Only draw coordinates near the edges.
                if col == 0:
                    rank = str(8 - row)

                    text = self.coordinate_font.render(
                        rank,
                        True,
                        self.get_coordinate_color(row, col)
                    )

                    self.screen.blit(
                        text,
                        (
                            col * self.square_size + 5,
                            row * self.square_size + 5
                        )
                    )

                if row == BOARD_SIZE - 1:
                    file_name = files[col]

                    text = self.coordinate_font.render(
                        file_name,
                        True,
                        self.get_coordinate_color(row, col)
                    )

                    text_rect = text.get_rect()

                    text_rect.bottomright = (
                        (col + 1) * self.square_size - 5,
                        (row + 1) * self.square_size - 5
                    )

                    self.screen.blit(
                        text,
                        text_rect
                    )

    def get_coordinate_color(
        self,
        row: int,
        col: int
    ) -> tuple[int, int, int]:
        """Return a readable coordinate color."""

        if (row + col) % 2 == 0:
            return DARK_SQUARE

        return LIGHT_SQUARE

    def draw_pieces(self, board: Board) -> None:
        """Draw all pieces currently on the board."""

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                piece = board.get_piece(row, col)

                if piece is not None:
                    rectangle = pygame.Rect(
                        col * self.square_size,
                        row * self.square_size,
                        self.square_size,
                        self.square_size,
                    )

                    self.draw_piece(
                        piece.symbol(),
                        rectangle
                    )

    def draw_piece(
        self,
        symbol: str,
        rectangle: pygame.Rect
    ) -> None:
        """Draw an individual chess piece."""

        # Draw the piece using a Unicode chess symbol.
        text = self.piece_font.render(
            symbol,
            True,
            (20, 20, 20)
        )

        text_rect = text.get_rect(
            center=rectangle.center
        )

        self.screen.blit(
            text,
            text_rect
        )
