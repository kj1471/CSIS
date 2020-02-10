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
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.roof_colour = (128, 128, 128)  # gray
        self.wall_colour = (64, 8, 8)  # dark red

    def draw(self, surface):
        roof_height = self.height / 3  # One third of the height of the house
        roof_middle_x = self.left + self.width / 2  # middle of x
        # is roof
        pygame.draw.rect(surface, self.wall_colour,
                         (  # left, top, width, height:
                             self.left, self.top + roof_height,
                             self.width, self.height - roof_height
                         ))
        pygame.draw.polygon(surface, self.roof_colour,
                            (  # three points of the roof
                                (self.left, self.top + roof_height),
                                (roof_middle_x, self.top),
                                (self.left + self.width, self.top + roof_height)
                            ))


class Dog(DrawableObject):
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.main_colour = (128, 128, 96)  # brown

    def draw(self, surface):
        body_width = int(self.width * (4 / 5))  # body 80% width
        body_top = int(self.top + self.height * (1 / 3))
        body_height = int(self.height * (1 / 3))
        head_rad = int(self.height * (1 / 4))
        pygame.draw.rect(surface, self.main_colour,
                         (  # left, top, width, height:
                             self.left, body_top, body_width, body_height
                         ))
        pygame.draw.circle(surface, self.main_colour,
                           (  # x, y
                               self.left + body_width, body_top
                           ), head_rad)


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
            House(100, 250, 200, 350),
            Dog(400, 500, 150, 100)
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
