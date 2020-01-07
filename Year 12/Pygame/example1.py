"""
An example of a PyGame game. Excluding comments, it contains 71 line,
and challenges the user to survive as long as possible avoiding the "bullets"
comining towards them.
@author Kieran Vickers
"""
import math
import sys
from datetime import datetime
from random import randrange

import pygame

# Set the constants for pygame
SIZE = WIDTH, HEIGHT = (800, 600)
CAPTION = "Pygame Example One"
BACKGROUND_COLOUR = (64, 0, 64)

# Initiate pygame and a screen to display to, using the constants
pygame.init()
pygame.font.init()  # This line isn't needed unless you write text to screen.
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption(CAPTION)

# Initialise the game
FRAMES_PER_SECOND = 30
FRAMES_BETWEEN_BULLET_SPAWN = FRAMES_PER_SECOND / 5  # 5 bullets per second
BULLET_SPEED = int(SIZE[0] / (FRAMES_PER_SECOND * 10))  # 10 seconds to cross
PLAYER_RADIUS = 20
BULLET_RADIUS = 10
PLAYER_COLOUR = (255, 255, 255)
BULLET_COLOUR = (255, 0, 0)

player_position = (0, 0)  # The current position of the player
frames_since_last_bullet = 0  # Count the number of frames between bullet spawns
# Four lists of bullet positions, one for each direction
bullets_going_right = []
bullets_going_down = []
bullets_going_left = []
bullets_going_up = []
# Store the time the player starts, so we can display a score
start_time = datetime.now()

#####################
# Run the game loop #
#####################
running = True
while running:
    ###############################
    # Handle any event that occur #
    ###############################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the event is a "QUIT" event, quit the game
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # If the mouse has moved at all...
            # (in this case, we now know this `event` will have a `.pos`
            # attribute, saying here the mouse is now
            player_position = event.pos  # Store the mouse position

    #########################
    # Update the game state #
    #########################

    # Update where all the bullets are now, by moving them in their direction
    for bullet_index, old_bullet_position in enumerate(bullets_going_right):
        bullet_x, bullet_y = old_bullet_position
        bullets_going_right[bullet_index] = (bullet_x + BULLET_SPEED, bullet_y)

    for bullet_index, old_bullet_position in enumerate(bullets_going_down):
        bullet_x, bullet_y = old_bullet_position
        bullets_going_down[bullet_index] = (bullet_x, bullet_y + BULLET_SPEED)

    for bullet_index, old_bullet_position in enumerate(bullets_going_left):
        bullet_x, bullet_y = old_bullet_position
        bullets_going_left[bullet_index] = (bullet_x - BULLET_SPEED, bullet_y)

    for bullet_index, old_bullet_position in enumerate(bullets_going_up):
        bullet_x, bullet_y = old_bullet_position
        bullets_going_up[bullet_index] = (bullet_x, bullet_y - BULLET_SPEED)

    # Test each bullet to see if the player has collided with it
    player_x, player_y = player_position
    for bullet_position in (bullets_going_right + bullets_going_down +
                            bullets_going_left + bullets_going_up):
        # The distance between two pixels can be calculated using Pythagoras,
        # as it can be considered a right angle triangle: the distance
        # between the xs, and the distance between the ys as the two known
        # edges, sqrt(x^2 + y^2).
        bullet_x, bullet_y = bullet_position
        x_distance = abs(player_x - bullet_x)
        y_distance = abs(player_y - bullet_y)
        if math.sqrt(x_distance ** 2 + y_distance ** 2) < \
                PLAYER_RADIUS + BULLET_RADIUS:
            running = False
            print("Game over.")
            time = (datetime.now() - start_time).total_seconds()
            print("Your score was:", time)

    # Add new bullet
    # Add one to the counter of number of frames since last bullet
    frames_since_last_bullet += 1
    # FRAMES_PER_SECOND / NEW_BULLETS_PER_SECOND is the calculation of frames
    # between bullet spawns, given these constants, if the number
    if frames_since_last_bullet == FRAMES_BETWEEN_BULLET_SPAWN:
        # If the number of frames since last bullet is the number of frames
        # between each bullet spawn:
        # Reset the counter,
        frames_since_last_bullet = 0
        # and add a new bullet to each direction
        bullets_going_right.append((0, randrange(HEIGHT)))
        bullets_going_down.append((randrange(WIDTH), 0))
        bullets_going_left.append((WIDTH, randrange(HEIGHT)))
        bullets_going_up.append((randrange(WIDTH), HEIGHT))

    ###############################
    # Draw the game to the screen #
    ###############################
    screen.fill(BACKGROUND_COLOUR)  # Fill background
    for bullet_position in (bullets_going_right + bullets_going_down +
                            bullets_going_left + bullets_going_up):
        pygame.draw.circle(screen, BULLET_COLOUR, bullet_position,
                           BULLET_RADIUS)
    pygame.draw.circle(screen, PLAYER_COLOUR, player_position, PLAYER_RADIUS)

    ############################################
    # Update the screen and wait for the clock #
    ############################################
    pygame.display.update()  # Display what we have drawn
    clock.tick(FRAMES_PER_SECOND)

# If no longer running, quit pygame and exit.
pygame.quit()
sys.exit(0)
