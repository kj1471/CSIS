"""
An example of a PyGame game. Excluding comments, it contains 91 line,
and challenges the user to survive as long as possible avoiding the "bullets"
comining towards them. This is identical to example1.py but written more OO.
@author Kieran Vickers
"""
import math
import sys
from datetime import datetime
from random import randrange
from typing import List, Any

import pygame

# Set the constants for pygame
SIZE = WIDTH, HEIGHT = (800, 600)
CAPTION = "Workshop1 Task2"
BACKGROUND_COLOUR = (64, 0, 64)

# Initialise the game
FRAMES_PER_SECOND = 30
FRAMES_BETWEEN_BULLET_SPAWN = FRAMES_PER_SECOND / 5  # 5 bullets per second
BULLET_SPEED = int(SIZE[0] / (FRAMES_PER_SECOND * 10))  # 10 seconds to cross
PLAYER_RADIUS = 20
BULLET_RADIUS = 10
PLAYER_COLOUR = (255, 255, 255)
BULLET_COLOUR = (255, 0, 0)


# Define a general "thing"
class Thing:
    def on_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


# Define a circle
class Circle(Thing):
    def __init__(self, starting_x, starting_y, radius, colour):
        self.position = (starting_x, starting_y)
        self.radius = radius
        self.colour = colour

    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position, self.radius)


# Define a Bullet object
class Bullet(Circle):
    """
    A Bullet is an object in the game, which can travel in one of four
    directions, starts from the end of the screen and continues forever.
    """
    # Define the different directions (as number 0 to 3)
    DIRECTIONS = RIGHT, DOWN, LEFT, UP = range(4)

    def __init__(self, direction):
        """
        Create a bullet object (initialise) given the direction it will
        travel in.
        @param direction: An integer representing the direction the bullet
        should travel in.
        """
        # Define the starting position and the amount to move given the
        # direction.
        if direction == Bullet.RIGHT:
            starting_x, starting_y = (0, randrange(HEIGHT))
            self.movement = (BULLET_SPEED, 0)
        elif direction == Bullet.DOWN:
            starting_x, starting_y = (randrange(WIDTH), 0)
            self.movement = (0, BULLET_SPEED)
        elif direction == Bullet.LEFT:
            starting_x, starting_y = (WIDTH, randrange(HEIGHT))
            self.movement = (-BULLET_SPEED, 0)
        else:
            starting_x, starting_y = (randrange(WIDTH), HEIGHT)
            self.movement = (0, -BULLET_SPEED)

        super().__init__(starting_x, starting_y, BULLET_RADIUS, BULLET_COLOUR)

    def update(self):
        """
        Update the position of the object.
        """
        old_x, old_y = self.position
        move_x, move_y = self.movement
        self.position = old_x + move_x, old_y + move_y

    def collision_test(self, user_position):
        """
        Test to see if this bullet has collided with the user.
        The distance between two pixels can be calculated using Pythagoras,
        as it can be considered a right angle triangle: the distance
        between the xs, and the distance between the ys as the two known
        edges, sqrt(x^2 + y^2).
        @param user_position: The x, y position of the user
        @return: A boolean, true if a collision has occurred.
        """
        x, y = self.position
        other_x, other_y = user_position
        return \
            math.sqrt(abs(x - other_x) ** 2 + abs(y - other_y) ** 2) < \
            PLAYER_RADIUS + BULLET_RADIUS


class Player(Circle):
    def __init__(self):
        super().__init__(WIDTH / 2, HEIGHT / 2,
                         PLAYER_RADIUS, PLAYER_COLOUR)

    def on_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # If the mouse has moved at all...
            # (in this case, we now know this `event` will have a `.pos`
            # attribute), saying here the mouse is now
            self.position = event.pos  # Store the mouse position


# Define the game
class ExampleGameTwo:
    """
    An example pygame game.
    """

    def __init__(self):
        # Create a list of all children. As long as these are all "Thing"s
        # then we can call on_event, update and draw regardless of inheritance.
        self.children = []

        # Initiate pygame and a screen to display to, using the constants
        pygame.init()
        pygame.font.init()  # Line isn't needed unless you write text to screen.
        pygame.display.set_caption(CAPTION)

        self.frames_since_last_bullet = 0  # Count the number of frames between
        # bullet spawns
        self.player = Player()
        self.children.append(self.player)  # Add player to children
        self.bullets = []

        self.start_time = datetime.now()

        # Store some pygame variables to the game too
        self.running = True
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()

    def event_handler(self, event):
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

        for bullet in self.bullets:
            if bullet.collision_test(self.player.position):
                self.running = False
                print("Game over.")
                time = (datetime.now() - self.start_time).total_seconds()
                print("Your score was:", time)

        # Add new bullets if time to
        # Add one to the counter of number of frames since last bullet
        self.frames_since_last_bullet += 1
        # FRAMES_PER_SECOND / NEW_BULLETS_PER_SECOND is the calculation of
        # frames between bullet spawns, given these constants, if the number
        if self.frames_since_last_bullet >= FRAMES_BETWEEN_BULLET_SPAWN:
            # If the number of frames since last bullet is the number of frames
            # between each bullet spawn:
            # Reset the counter,
            self.frames_since_last_bullet = 0
            # and add a new bullet to each direction
            for direction in Bullet.DIRECTIONS:
                new_bullet = Bullet(direction=direction)
                self.bullets.append(new_bullet)
                self.children.append(new_bullet)

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
                    self.event_handler(event)

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
    game = ExampleGameTwo()
    game.run_game()
