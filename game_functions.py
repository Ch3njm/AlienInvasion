import pygame

def check_keydown_events(event, ship):
     if event.key == pygame.K_RIGHT:
          #move the ship right
          ship.moving_right = True
     elif event.key == pygame.K_LEFT:
          ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return 0
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """update the window and switch to new window"""
    #redraw the window in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #print the window 
    pygame.display.flip()
