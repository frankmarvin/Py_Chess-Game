from typing import Optional

from game.piece import Piece, PieceColor, PieceType


class Board:
    """Represents the 8x8 chess board."""

    def __init__(self) -> None:
        self.grid: list[list[Optional[Piece]]] = [
            [None for _ in range(8)] for _ in range(8)
        ]

        self.setup_board()

    def setup_board(self) -> None:
        """Place all 32 chess pieces in their starting positions."""

        # Clear the board first
        self.grid = [
            [None for _ in range(8)] for _ in range(8)
        ]

        # Black pieces
        self.grid[0] = [
            Piece(PieceColor.BLACK, PieceType.ROOK),
            Piece(PieceColor.BLACK, PieceType.KNIGHT),
            Piece(PieceColor.BLACK, PieceType.BISHOP),
            Piece(PieceColor.BLACK, PieceType.QUEEN),
            Piece(PieceColor.BLACK, PieceType.KING),
            Piece(PieceColor.BLACK, PieceType.BISHOP),
            Piece(PieceColor.BLACK, PieceType.KNIGHT),
            Piece(PieceColor.BLACK, PieceType.ROOK),
        ]

        # Black pawns
        for col in range(8):
            self.grid[1][col] = Piece(
                PieceColor.BLACK,
                PieceType.PAWN
            )

        # White pawns
        for col in range(8):
            self.grid[6][col] = Piece(
                PieceColor.WHITE,
                PieceType.PAWN
            )

        # White pieces
        self.grid[7] = [
            Piece(PieceColor.WHITE, PieceType.ROOK),
            Piece(PieceColor.WHITE, PieceType.KNIGHT),
            Piece(PieceColor.WHITE, PieceType.BISHOP),
            Piece(PieceColor.WHITE, PieceType.QUEEN),
            Piece(PieceColor.WHITE, PieceType.KING),
            Piece(PieceColor.WHITE, PieceType.BISHOP),
            Piece(PieceColor.WHITE, PieceType.KNIGHT),
            Piece(PieceColor.WHITE, PieceType.ROOK),
        ]

    def get_piece(
        self,
        row: int,
        col: int
    ) -> Optional[Piece]:
        """Return the piece at a specific board position."""

        if not self.is_valid_square(row, col):
            return None

        return self.grid[row][col]

    def set_piece(
        self,
        row: int,
        col: int,
        piece: Optional[Piece]
    ) -> None:
        """Place or remove a piece from a board position."""

        if self.is_valid_square(row, col):
            self.grid[row][col] = piece

    def move_piece(
        self,
        start_row: int,
        start_col: int,
        end_row: int,
        end_col: int
    ) -> bool:
        """
        Move a piece from one square to another.

        This method currently performs the basic board operation.
        Chess movement rules will be implemented later.
        """

        if not self.is_valid_square(start_row, start_col):
            return False

        if not self.is_valid_square(end_row, end_col):
            return False

        piece = self.get_piece(start_row, start_col)

        if piece is None:
            return False

        self.set_piece(end_row, end_col, piece)
        self.set_piece(start_row, start_col, None)

        return True

    def is_valid_square(self, row: int, col: int) -> bool:
        """Check whether a position is inside the chess board."""

        return 0 <= row < 8 and 0 <= col < 8

    def reset(self) -> None:
        """Reset the board to the starting position."""

        self.setup_board()

    def get_all_pieces(self) -> list[Piece]:
        """Return all pieces currently on the board."""

        pieces: list[Piece] = []

        for row in self.grid:
            for piece in row:
                if piece is not None:
                    pieces.append(piece)

        return pieces

    def count_pieces(self) -> int:
        """Return the number of pieces currently on the board."""

        return len(self.get_all_pieces())
