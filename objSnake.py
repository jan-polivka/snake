import pygame
import os
import random

snake_image = os.path.join("D:\interview_prep\python\snake", "snake_image.png")


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.image = pygame.image.load(snake_image)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.next = None

        self.prevX = x
        self.prevY = y

        self.movX = screen.get_width()/10
        self.movY = screen.get_height()/10

        self.maxX = screen.get_width()-10
        self.maxY = screen.get_height()-10

    def coords(self):
        print("{} {}".format(self.rect.x, self.rect.y))
#        return {self.rect.x, self.rect.y}

    def collide(self, otherSprite):
        return self.rect.colliderect(otherSprite)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.next:
            self.next.draw(screen)

    def advance(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.prevX, self.prevY = self.rect.x, self.rect.y
            self.rect.y -= self.movY
            if self.next:
                self.next.propMov(self.prevX, self.prevY)
        elif pressed[pygame.K_DOWN]:
            self.prevX, self.prevY = self.rect.x, self.rect.y
            self.rect.y += self.movY
            if self.next:
                self.next.propMov(self.prevX, self.prevY)
        elif pressed[pygame.K_RIGHT]:
            self.prevX, self.prevY = self.rect.x, self.rect.y
            self.rect.x += self.movX
            if self.next:
                self.next.propMov(self.prevX, self.prevY)
        elif pressed[pygame.K_LEFT]:
            self.prevX, self.prevY = self.rect.x, self.rect.y
            self.rect.x -= self.movX
            if self.next:
                self.next.propMov(self.prevX, self.prevY)

    def propMov(x, y):
        self.prevX, self.prevY = self.x, self.y
        self.rect.x, self.rect.y = x, y
        if self.next:
            self.next.propMov(self.prevX, self.prevY)


    def addLink(self):
        if self.next:
            self.next.addLink()
        else:
            self.next = Snake(self.prevX, self.prevY)


    def respawn(self):
        self.rect.x = 50*random.randint(0,8) + 25
        self.rect.y = 50*random.randint(0,8) + 25


