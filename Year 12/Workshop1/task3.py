"""
An example of a PyGame game. Excluding comments, it contains 91 line,
and challenges the user to survive as long as possible avoiding the "bullets"
comining towards them. This is identical to example1.py but written more OO.
@author Kieran Vickers
"""
import sys

import pygame

# Set the constants for pygame
SIZE = WIDTH, HEIGHT = (800, 600)
CAPTION = "Workshop1 Task3"
BACKGROUND_COLOUR = (64, 64, 64)
FRAMES_PER_SECOND = 20


# Define a general "thing"
class DrawableObject:
    def on_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


########################################
# CREATE YOUR OWN DRAWABLEOBJECTS HERE #
########################################

class House(DrawableObject):
    pass


class Dog(DrawableObject):
    pass


# Define the game
class ExampleGameThree(DrawableObject):
    """
    An example pygame game.
    """

    def __init__(self):
        # Create a list of all children. As long as these are all "Thing"s
        # then we can call on_event, update and draw regardless of inheritance.
        self.children = [
            # List all the objects you want to draw here.
        ]

        # Initiate pygame and a screen to display to, using the constants
        pygame.init()
        pygame.font.init()  # Line isn't needed unless you write text to screen.
        pygame.display.set_caption(CAPTION)

        # Store some pygame variables to the game too
        self.running = True
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()

    def on_event(self, event):
        """
        The event handler for this game, called once for every (non QUIT)
        event, after a draw and before the update. Currently handles
        MOUSEMOTION only.
        @param event: Any pygame event.
        """
        for child in self.children:
            child.on_event(event)

    def update(self):
        """
        Update the state of the game, called each frame after events handled
        before drawing to the screen.
        This function moves all bullets, checks for collisions (end game),
        and adds new bullets.
        """
        for child in self.children:
            child.update()

    def draw(self, surface: pygame.Surface):
        """
        Draw all this game to the surface.
        @param surface: A surface to draw the game to.
        """
        for child in self.children:
            child.draw(surface)

    def run_game(self):
        """
        Run the game, this function is independent of the game logic,
        and therefore might not need changed.
        """
        # Run the game loop
        while self.running:
            # Handle any event that occur
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the event is a "QUIT" event, quit the game
                    self.running = False
                else:
                    # Otherwise, allow the event handler to handle the event
                    self.on_event(event)

            # Update the game state
            self.update()

            # Draw the game to the screen
            self.screen.fill(BACKGROUND_COLOUR)  # Fill background
            self.draw(self.screen)

            # Update and wait
            pygame.display.update()  # Display what we have drawn
            self.clock.tick(FRAMES_PER_SECOND)
        # If no longer running, quit pygame and exit.
        pygame.quit()
        sys.exit(0)


if __name__ == '__main__':
    game = ExampleGameThree()
    game.run_game()
