import pygame
import os
import random

apple_image = os.path.join("D:\interview_prep\python\snake", "apple_image.png")
random.seed()

class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load(apple_image)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x,y

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def coords(self):
        return {self.rect.x, self.rect.y}

    def respawn(self):
        self.rect.x, self.rect.y = random.randint(1,10), random.randint(1,10)
