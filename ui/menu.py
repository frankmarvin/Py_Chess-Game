import pygame

from utils.constants import WINDOW_HEIGHT, WINDOW_WIDTH


class Menu:
    """Main menu for the chess game."""

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        # Fonts
        self.title_font = pygame.font.SysFont(
            "dejavusans",
            64,
            bold=True
        )

        self.button_font = pygame.font.SysFont(
            "dejavusans",
            32,
            bold=True
        )

        # Button dimensions
        self.button_width = 260
        self.button_height = 60

        self.start_button = pygame.Rect(
            (WINDOW_WIDTH - self.button_width) // 2,
            320,
            self.button_width,
            self.button_height
        )

        self.quit_button = pygame.Rect(
            (WINDOW_WIDTH - self.button_width) // 2,
            410,
            self.button_width,
            self.button_height
        )

    def draw(self) -> None:
        """Draw the main menu."""

        self.screen.fill((30, 30, 30))

        # Draw title
        title = self.title_font.render(
            "♟ Python Chess",
            True,
            (240, 240, 240)
        )

        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, 180)
        )

        self.screen.blit(title, title_rect)

        # Draw buttons
        self.draw_button(
            self.start_button,
            "Start Game"
        )

        self.draw_button(
            self.quit_button,
            "Quit"
        )

        pygame.display.flip()

    def draw_button(
        self,
        rectangle: pygame.Rect,
        text: str
    ) -> None:
        """Draw a menu button."""

        mouse_position = pygame.mouse.get_pos()

        if rectangle.collidepoint(mouse_position):
            button_color = (100, 100, 100)
        else:
            button_color = (70, 70, 70)

        pygame.draw.rect(
            self.screen,
            button_color,
            rectangle,
            border_radius=10
        )

        pygame.draw.rect(
            self.screen,
            (180, 180, 180),
            rectangle,
            width=2,
            border_radius=10
        )

        text_surface = self.button_font.render(
            text,
            True,
            (255, 255, 255)
        )

        text_rectangle = text_surface.get_rect(
            center=rectangle.center
        )

        self.screen.blit(
            text_surface,
            text_rectangle
        )

    def handle_event(self, event: pygame.event.Event) -> str | None:
        """Handle menu events.

        Returns:
            'start' when Start Game is selected.
            'quit' when Quit is selected.
            None when there is no menu action.
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if self.start_button.collidepoint(event.pos):
                    return "start"

                if self.quit_button.collidepoint(event.pos):
                    return "quit"

        return None
