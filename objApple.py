import pygame
import os
import random
import math

apple_image = os.path.join("D:\snake", "apple_image.png")
random.seed()

class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.image = pygame.image.load(apple_image)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x,y

        self.maxX = screen.get_width() - 10
        self.maxY = screen.get_height() - 10

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def respawn(self):
        self.rect.x = 50*random.randint(0,8) + 25
        self.rect.y = 50*random.randint(0,8) + 25

        
