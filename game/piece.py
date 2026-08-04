from dataclasses import dataclass
from enum import Enum


class PieceColor(Enum):
    """The two possible chess piece colors."""

    WHITE = "white"
    BLACK = "black"


class PieceType(Enum):
    """The six types of chess pieces."""

    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
    KNIGHT = "knight"
    PAWN = "pawn"


@dataclass
class Piece:
    """Represents a chess piece."""

    color: PieceColor
    piece_type: PieceType

    def symbol(self) -> str:
        """Return the Unicode symbol for the piece."""

        symbols = {
            # White pieces
            (PieceColor.WHITE, PieceType.KING): "♔",
            (PieceColor.WHITE, PieceType.QUEEN): "♕",
            (PieceColor.WHITE, PieceType.ROOK): "♖",
            (PieceColor.WHITE, PieceType.BISHOP): "♗",
            (PieceColor.WHITE, PieceType.KNIGHT): "♘",
            (PieceColor.WHITE, PieceType.PAWN): "♙",

            # Black pieces
            (PieceColor.BLACK, PieceType.KING): "♚",
            (PieceColor.BLACK, PieceType.QUEEN): "♛",
            (PieceColor.BLACK, PieceType.ROOK): "♜",
            (PieceColor.BLACK, PieceType.BISHOP): "♝",
            (PieceColor.BLACK, PieceType.KNIGHT): "♞",
            (PieceColor.BLACK, PieceType.PAWN): "♟",
        }

        return symbols[(self.color, self.piece_type)]

    def is_white(self) -> bool:
        """Return True if the piece is white."""

        return self.color == PieceColor.WHITE

    def is_black(self) -> bool:
        """Return True if the piece is black."""

        return self.color == PieceColor.BLACK

    def __str__(self) -> str:
        """Return the piece's chess symbol."""

        return self.symbol()
