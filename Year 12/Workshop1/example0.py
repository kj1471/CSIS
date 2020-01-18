"""
A really simple example of a PyGame game. Excluding comments, it contains 18
line, and does nothing.
@author Kieran Vickers
"""
import sys

import pygame

# Set the constants for pygame
SIZE = (800, 600)
CAPTION = "Workshop1 Example Zero"
BACKGROUND_COLOUR = (64, 0, 64)

# Initiate pygame and a screen to display to, using the constants
pygame.init()
pygame.font.init()  # This line isn't needed unless you write text to screen.
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption(CAPTION)

# Initialise the game
FRAMES_PER_SECOND = 30
# ADD OTHER GAME CONSTANTS HERE ************************************************
# ADD VARIABLES AND INITIALISE THEM HERE ***************************************

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

        # HANDLE OTHER EVENTS HERE *********************************************

    #########################
    # Update the game state #
    #########################

    # UPDATE THE GAME STATE HERE ***********************************************

    ###############################
    # Draw the game to the screen #
    ###############################
    screen.fill(BACKGROUND_COLOUR)  # Fill background

    # DRAW TO THE SCREEN HERE **************************************************

    ############################################
    # Update the screen and wait for the clock #
    ############################################
    pygame.display.update()  # Display what we have drawn
    clock.tick(FRAMES_PER_SECOND)

# If no longer running, quit pygame and exit.
pygame.quit()
sys.exit(0)
