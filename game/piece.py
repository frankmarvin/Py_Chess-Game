from dataclasses import dataclass
from enum import Enum


class PieceColor(Enum):
    WHITE = "white"
    BLACK = "black"


class PieceType(Enum):
    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    BISHOP = "bishop"
    KNIGHT = "knight"
    PAWN = "pawn"


@dataclass
class Piece:
    color: PieceColor
    piece_type: PieceType

    def symbol(self) -> str:
        """Return the Unicode symbol for the chess piece."""

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

    def __str__(self) -> str:
        """Return the piece symbol when converted to text."""
        return self.symbol()
