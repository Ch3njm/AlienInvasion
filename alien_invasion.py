import sys

import pygame
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")


    #start the main loop of the game
    while True:

        #monitor the mouse and keyborad event
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        #display recent screen
        pygame.display.flip()


run_game()
