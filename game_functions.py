import pygame

def check_events():

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                
def update_screen(ai_settings, screen, ship):
    """update the window and switch to new window"""
    #redraw the window in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #print the window 
    pygame.display.flip()
