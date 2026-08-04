import unittest

from game.board import Board
from game.piece import PieceColor, PieceType


class TestBoard(unittest.TestCase):
    """Tests for the chess board."""

    def setUp(self) -> None:
        self.board = Board()

    def test_board_has_eight_rows(self) -> None:
        """The chess board must contain 8 rows."""

        self.assertEqual(
            len(self.board.grid),
            8
        )

    def test_board_has_eight_columns(self) -> None:
        """Every row must contain 8 squares."""

        for row in self.board.grid:
            self.assertEqual(
                len(row),
                8
            )

    def test_board_has_64_squares(self) -> None:
        """The chess board must contain 64 squares."""

        total_squares = sum(
            len(row)
            for row in self.board.grid
        )

        self.assertEqual(
            total_squares,
            64
        )

    def test_valid_square(self) -> None:
        """Test valid board coordinates."""

        self.assertTrue(
            self.board.is_valid_square(0, 0)
        )

        self.assertTrue(
            self.board.is_valid_square(7, 7)
        )

        self.assertTrue(
            self.board.is_valid_square(3, 4)
        )

    def test_invalid_square(self) -> None:
        """Test coordinates outside the board."""

        self.assertFalse(
            self.board.is_valid_square(-1, 0)
        )

        self.assertFalse(
            self.board.is_valid_square(0, 8)
        )

        self.assertFalse(
            self.board.is_valid_square(8, 8)
        )

    def test_get_empty_square(self) -> None:
        """Test getting a piece from an empty square."""

        piece = self.board.get_piece(3, 3)

        self.assertIsNone(piece)

    def test_initial_piece_count(self) -> None:
        """The initial board should contain 32 pieces."""

        pieces = []

        for row in self.board.grid:
            for piece in row:
                if piece is not None:
                    pieces.append(piece)

        self.assertEqual(
            len(pieces),
            32
        )

    def test_white_piece_count(self) -> None:
        """White should start with 16 pieces."""

        white_pieces = []

        for row in self.board.grid:
            for piece in row:
                if (
                    piece is not None
                    and piece.color == PieceColor.WHITE
                ):
                    white_pieces.append(piece)

        self.assertEqual(
            len(white_pieces),
            16
        )

    def test_black_piece_count(self) -> None:
        """Black should start with 16 pieces."""

        black_pieces = []

        for row in self.board.grid:
            for piece in row:
                if (
                    piece is not None
                    and piece.color == PieceColor.BLACK
                ):
                    black_pieces.append(piece)

        self.assertEqual(
            len(black_pieces),
            16
        )

    def test_white_king_position(self) -> None:
        """White king should start at e1."""

        piece = self.board.get_piece(7, 4)

        self.assertIsNotNone(piece)
        self.assertEqual(piece.color, PieceColor.WHITE)
        self.assertEqual(piece.piece_type, PieceType.KING)

    def test_black_king_position(self) -> None:
        """Black king should start at e8."""

        piece = self.board.get_piece(0, 4)

        self.assertIsNotNone(piece)
        self.assertEqual(piece.color, PieceColor.BLACK)
        self.assertEqual(piece.piece_type, PieceType.KING)


if __name__ == "__main__":
    unittest.main()
