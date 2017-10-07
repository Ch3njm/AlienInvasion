import pygame

class Ship():

    def __init__(self,screen):
        #initialize the ship and its location
        self.screen = screen

        #load image and get the rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put every ship in the center of screen bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #print ship in a designated spot
        self.screen.blit(self.image, self.rect)
