import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    
    #start the main loop of the game
    while True:

        
        gf.update_screen(ai_settings, screen, ship)
        ship.update()
        #monitor the mouse and keyborad event
        if gf.check_events(ship)==0:
            break

run_game()
