import pygame

from game.board import Board
from utils.constants import (
    BOARD_SIZE,
    SQUARE_SIZE,
    LIGHT_SQUARE,
    DARK_SQUARE,
    SELECTED_SQUARE,
    LEGAL_MOVE,
    CAPTURE_MOVE,
    TEXT_COLOR,
    PIECE_FONT,
    PIECE_FONT_SIZE,
)


class BoardView:
    """Handles the graphical display of the chess board."""

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        self.selected_square = None
        self.legal_moves = []

        self.piece_font = pygame.font.SysFont(
            PIECE_FONT,
            PIECE_FONT_SIZE
        )

        self.coordinate_font = pygame.font.SysFont(
            "dejavusans",
            14
        )

    def draw(self, board: Board) -> None:
        """Draw the complete chess board."""

        self.draw_squares()
        self.draw_coordinates()
        self.draw_pieces(board)

    def draw_squares(self) -> None:
        """Draw all 64 chess squares."""

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                if (row + col) % 2 == 0:
                    square_color = LIGHT_SQUARE
                else:
                    square_color = DARK_SQUARE

                rectangle = pygame.Rect(
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )

                pygame.draw.rect(
                    self.screen,
                    square_color,
                    rectangle
                )

                # Highlight selected square.
                if self.selected_square == (row, col):
                    pygame.draw.rect(
                        self.screen,
                        SELECTED_SQUARE,
                        rectangle
                    )

                # Highlight legal moves.
                if (row, col) in self.legal_moves:
                    pygame.draw.circle(
                        self.screen,
                        LEGAL_MOVE,
                        rectangle.center,
                        10
                    )

    def draw_pieces(self, board: Board) -> None:
        """Draw all chess pieces."""

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                piece = board.get_piece(
                    row,
                    col
                )

                if piece is None:
                    continue

                symbol = piece.symbol()

                text = self.piece_font.render(
                    symbol,
                    True,
                    TEXT_COLOR
                )

                rectangle = pygame.Rect(
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )

                text_rectangle = text.get_rect(
                    center=rectangle.center
                )

                self.screen.blit(
                    text,
                    text_rectangle
                )

    def draw_coordinates(self) -> None:
        """Draw chess board coordinates."""

        files = "abcdefgh"
        ranks = "87654321"

        for col in range(BOARD_SIZE):

            file_text = self.coordinate_font.render(
                files[col],
                True,
                TEXT_COLOR
            )

            self.screen.blit(
                file_text,
                (
                    col * SQUARE_SIZE + 5,
                    BOARD_SIZE * SQUARE_SIZE - 20
                )
            )

        for row in range(BOARD_SIZE):

            rank_text = self.coordinate_font.render(
                ranks[row],
                True,
                TEXT_COLOR
            )

            self.screen.blit(
                rank_text,
                (
                    5,
                    row * SQUARE_SIZE + 5
                )
            )

    def select_square(
        self,
        row: int,
        col: int
    ) -> None:
        """Select a chess square."""

        self.selected_square = (row, col)

    def clear_selection(self) -> None:
        """Clear the current square selection."""

        self.selected_square = None
        self.legal_moves = []

    def set_legal_moves(
        self,
        moves: list[tuple[int, int]]
    ) -> None:
        """Set the squares that can currently be moved to."""

        self.legal_moves = moves

    def get_square_from_mouse(
        self,
        mouse_position: tuple[int, int]
    ) -> tuple[int, int] | None:
        """Convert mouse coordinates into board coordinates."""

        mouse_x, mouse_y = mouse_position

        col = mouse_x // SQUARE_SIZE
        row = mouse_y // SQUARE_SIZE

        if (
            0 <= row < BOARD_SIZE
            and 0 <= col < BOARD_SIZE
        ):
            return row, col

        return None
