import pygame
from pygame.locals import *

def redraw(screen):
     # Fill background
    screen.fill((250, 250, 250))
    pygame.display.update()

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Basic Pygame program')

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))

    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        redraw(screen)


if __name__ == '__main__': main()