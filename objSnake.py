import pygame
import os

snake_image = os.path.join("D:\interview_prep\python\snake", "snake_image.png")


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load(snake_image)
        self.rect = self.image.get_rect()

        self.x = x
        self.rect.x = x
        self.y = y
        self.rect.y = y
        self.next = None

        self.prevX = x
        self.prevY = y

    def coords(self):
        return {self.x, self.y}

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.next:
            self.next.draw(screen)

    def advance(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.prevX, self.prevY = self.x, self.y
            self.y -= 10
            self.rect.y -= 10
            if self.next:
                self.next.propMov(self.prevX, self.prevY)
        elif pressed[pygame.K_DOWN]:
            self.prevX, self.prevY = self.x, self.y
            self.y += 10
            self.rect.y += 10
            if self.next:
                self.next.propMov(self.prevX, self.prevY)
        elif pressed[pygame.K_RIGHT]:
            self.prevX, self.prevY = self.x, self.y
            self.x += 10
            self.rect.x += 10
            if self.next:
                self.next.propMov(self.prevX, self.prevY)
        elif pressed[pygame.K_LEFT]:
            self.prevX, self.prevY = self.x, self.y
            self.x -= 10
            self.rect.x -= 10
            if self.next:
                self.next.propMov(self.prevX, self.prevY)

    def propMov(x, y):
        self.prevX, self.prevY = self.x, self.y
        self.x, self.y = x, y
        if self.next:
            self.next.propMov(self.prevX, self.prevY)


    def addLink(self):
        if self.next:
            self.next.addLink()
        else:
            self.next = Snake(self.prevX, self.prevY)

