import sys

import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    flag = 1
    
    #start the main loop of the game
    while flag:

        
        screen.fill(bg_color)
        
        #display recent screen
        pygame.display.flip()

        #monitor the mouse and keyborad event
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flag = 0

                    
        
run_game()
