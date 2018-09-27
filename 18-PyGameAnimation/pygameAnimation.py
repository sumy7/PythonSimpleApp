import sys
import time

import pygame
from pygame.locals import *

# Window variables.
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Direction variables.
DOWN_LEFT = "downleft"
DOWN_RIGHT = "downright"
UP_LEFT = "upleft"
UP_RIGHT = "upright"

MOVE_SPEED = 4

# Colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the box data structure.
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UP_RIGHT}
b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir': UP_LEFT}
b3 = {'rect': pygame.Rect(100, 100, 60, 60), 'color': BLUE, 'dir': DOWN_LEFT}
boxes = [b1, b2, b3]

# Set up pygame.
pygame.init()

if __name__ == '__main__':
    # Set up the window.
    windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption('Animation')

    # Run the game loop.
    while True:
        # Check for the QUIT event.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw the white background onto the surface.
        windowSurface.fill(WHITE)

        for b in boxes:
            # Move the box data structure.
            if b['dir'] == DOWN_LEFT:
                b['rect'].left -= MOVE_SPEED
                b['rect'].top += MOVE_SPEED
            if b['dir'] == DOWN_RIGHT:
                b['rect'].left += MOVE_SPEED
                b['rect'].top += MOVE_SPEED
            if b['dir'] == UP_LEFT:
                b['rect'].left -= MOVE_SPEED
                b['rect'].top -= MOVE_SPEED
            if b['dir'] == UP_RIGHT:
                b['rect'].left += MOVE_SPEED
                b['rect'].top -= MOVE_SPEED

            # Check whether the box has moved out of the window.
            if b['rect'].top < 0:
                # The box has moved past the top.
                if b['dir'] == UP_LEFT:
                    b['dir'] = DOWN_LEFT
                if b['dir'] == UP_RIGHT:
                    b['dir'] = DOWN_RIGHT
            if b['rect'].bottom > WINDOW_HEIGHT:
                # The box has moved past the left side.
                if b['dir'] == DOWN_LEFT:
                    b['dir'] = UP_LEFT
                if b['dir'] == DOWN_RIGHT:
                    b['dir'] = UP_RIGHT
            if b['rect'].left < 0:
                # The box has moved past the left side.
                if b['dir'] == DOWN_LEFT:
                    b['dir'] = DOWN_RIGHT
                if b['dir'] == UP_LEFT:
                    b['dir'] = UP_RIGHT
            if b['rect'].right > WINDOW_WIDTH:
                # The box has moved past the right side.
                if b['dir'] == DOWN_RIGHT:
                    b['dir'] = DOWN_LEFT
                if b['dir'] == UP_RIGHT:
                    b['dir'] = UP_LEFT

            # Draw the box onto the surface.
            pygame.draw.rect(windowSurface, b['color'], b['rect'])

        # Draw the window onto the screen.
        pygame.display.update()
        time.sleep(0.02)
