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

    def advanceComputer(self, move):
        if move == "down":
            self.complexDown()
        elif move == "left":
            self.complexLeft()
        elif move == "right":
            self.complexRight()
        elif move == "up":
            self.complexUp()

    def advanceHuman(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            return self.complexDown()
        elif pressed[pygame.K_LEFT]:
            return self.complexLeft()
        elif pressed[pygame.K_RIGHT]:
            return self.complexRight()
        elif pressed[pygame.K_UP]:
            return self.complexUp()

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

            return True

    def addLink(self):
        if self.next:
            self.next.addLink()
        else:
            self.next = Link(self.prevX, self.prevY, self.screen)

    def checkAround(self, wall):
        detections = [0.0] * 4
        self.simpleLeft()
        if not self.rect.colliderect(wall) or self.collideItself():
            detections[0] = -1.0
        else:
            detections[0] = 1.0
        self.simpleRight()
        self.simpleRight()
        if not self.rect.colliderect(wall) or self.collideItself():
            detections[1] = -1.0
        else:
            detections[1] = 1.0
        self.simpleLeft()
        self.simpleUp()
        if not self.rect.colliderect(wall) or self.collideItself():
            detections[2] = -1.0
        else:
            detections[2] = 1.0
        self.simpleDown()
        self.simpleDown()
        if not self.rect.colliderect(wall) or self.collideItself():
            detections[3] = -1.0
        else:
            detections[3] = 1.0
        self.simpleUp()
        return detections

    def coords(self):
        return self.rect.x, self.rect.y

    def collide(self, otherSprite):
        return self.rect.colliderect(otherSprite)

    def collideItself(self):
        if not self.next:
            return False
        else:
            return self.next.collideHead(self)


    def complexDown(self):
        self.lastDir = "down"
        if self.next:
            self.simpleDown()
            if self.rect.colliderect(self.next):
                return False
            else:
                self.simpleUp()
                self.moveDown()
                return True
        else:
            self.moveDown()
            return True

    def complexLeft(self):
        self.lastDir = "left"
        if self.next:
            self.simpleLeft()
            if self.rect.colliderect(self.next):
                return False
            else:
                self.simpleRight()
                self.moveLeft()
                return True
        else:
            self.moveLeft()
            return True

    def complexRight(self):
        self.lastDir = "right"
        if self.next:
            self.simpleRight()
            if self.rect.colliderect(self.next):
                return False
            else:
                self.simpleLeft()
                self.moveRight()
                return True
        else:
            self.moveRight()
            return True

    def complexUp(self):
        self.lastDir = "up"
        if self.next:
            self.simpleUp()
            if self.rect.colliderect(self.next):
                return False
            else:
                self.simpleDown()
                self.moveUp()
                return True
        else:
            self.moveUp()
            return True

    def coords(self):
        print("snake: " + str(self.rect.x) + ", " + str(self.rect.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.next:
            self.next.draw(screen)


    def respawn(self):
        self.rect.x = 50*random.randint(2,6) + 25
        self.rect.y = 50*random.randint(2,6) + 25
        self.lastDir = None
        if self.next:
            self.next.deallocate()

        self.addLink()

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


    def simpleLeft(self):
        self.rect.x -= self.movX

    def simpleRight(self):
        self.rect.x += self.movX

    def simpleUp(self):
        self.rect.y -= self.movY

    def simpleDown(self):
        self.rect.y += self.movY


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
