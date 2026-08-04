from dataclasses import dataclass


@dataclass
class Player:
    """
    Represents a chess player.
    """

    name: str
    color: str

    def is_white(self) -> bool:
        """Return True if the player is White."""
        return self.color.lower() == "white"

    def is_black(self) -> bool:
        """Return True if the player is Black."""
        return self.color.lower() == "black"

    def __str__(self) -> str:
        """Return a readable player description."""
        return f"{self.name} ({self.color})"
