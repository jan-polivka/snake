import pygame
import os
import random

snake_image = os.path.join("D:\snake", "snake_image.png")
link_image = os.path.join("D:\snake", "link_image.png")


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

        self.lastDir = None

        self.screen = screen

    def coords(self):
#        print("{} {}".format(self.rect.x, self.rect.y))
        return self.rect.x, self.rect.y

    def collide(self, otherSprite):
        return self.rect.colliderect(otherSprite)

    def collideItself(self):
        if not self.next:
            return False
        else:
            return self.next.collideHead(self)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.next:
            self.next.draw(screen)

    def advance(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.moveUp()
            self.lastDir = "up"
        elif pressed[pygame.K_DOWN]:
            self.moveDown()
            self.lastDir = "down"
        elif pressed[pygame.K_RIGHT]:
            self.moveRight()
            self.lastDir = "right"
        elif pressed[pygame.K_LEFT]:
            self.moveLeft()
            self.lastDir = "left"

        else:
            if not self.lastDir:
                dirs = ["up", "down", "left", "right"]
                self.lastDir = random.choice(dirs)

            if self.lastDir == "up":
                self.moveUp()
            elif self.lastDir == "down": 
                self.moveDown()
            elif self.lastDir == "right":
                self.moveRight()
            elif self.lastDir == "left":
                self.moveLeft()

    def addLink(self):
        if self.next:
            self.next.addLink()
        else:
            self.next = Link(self.prevX, self.prevY, self.screen)

    def respawn(self):
        self.rect.x = 50*random.randint(2,6) + 25
        self.rect.y = 50*random.randint(2,6) + 25
        self.lastDir = None
        if self.next:
            self.next.deallocate()
            self.next = None

    def lastMove(self):
        return self.lastDir

    def moveLeft(self):
        self.prevX, self.prevY = self.rect.x, self.rect.y
        self.rect.x -= self.movX
        if self.next:
            self.next.propMov(self.prevX, self.prevY)

    def moveRight(self):
        self.prevX, self.prevY = self.rect.x, self.rect.y
        self.rect.x += self.movX
        if self.next:
            self.next.propMov(self.prevX, self.prevY)


    def moveUp(self):
        self.prevX, self.prevY = self.rect.x, self.rect.y
        self.rect.y -= self.movY
        if self.next:
            self.next.propMov(self.prevX, self.prevY)


    def moveDown(self):
        self.prevX, self.prevY = self.rect.x, self.rect.y
        self.rect.y += self.movY
        if self.next:
            self.next.propMov(self.prevX, self.prevY)


class Link(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        self.image = pygame.image.load(link_image)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.next = None

        self.prevX = x
        self.prevY = y

        self.screen = screen

    def addLink(self):
        if self.next:
            self.next.addLink()
        else:
            self.next = Link(self.prevX, self.prevY, self.screen)
 
    def collideHead(self, head):
        if not self.next:
            return False
        else:
            if self.rect.colliderect(head):
                return True
            else:
                return self.next.collideHead(head)

    def deallocate(self):
        if self.next == None:
            pass
        else:
            self.next.deallocate()
            self.next = None       


    def propMov(self, x, y):
        self.prevX, self.prevY = self.rect.x, self.rect.y
        self.rect.x, self.rect.y = x, y
        if self.next:
            self.next.propMov(self.prevX, self.prevY)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.next:
            self.next.draw(screen)
