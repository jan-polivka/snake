import pygame
import os

wall_image = os.path.join("D:\snake", "wall_image.png")


class Wall(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.image = pygame.image.load(wall_image)
        self.rect = self.image.get_rect()

#        self.rect.x = screen.get_width()/50
#        self.rect.y = screen.get_height()/50
        self.rect.x = 25
        self.rect.y = 25


    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
