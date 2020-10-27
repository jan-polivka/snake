import pygame #is this double import a problem?
import sys

from train import predict

import random

import copy

def game_predict(apple, clock, db, net, screen, snake, wall):
    quitCheck()

    state = snake.checkAround(wall)
    dirList = ["left","right","up","down"]
    selecting = True
    randSel = 0
    state.append(randSel)
    while selecting == True:
        randSel = random.randint(0,3)
        state[-1] = randSel
        print (state)
        move = predict(net, state)
        if not move:
            selecting = False

    snake.advanceComputer(dirList[randSel])

    if snake.collide(apple):
        apple.respawn()
        snake.addLink()
        #db.apple(apple.coords())

    if snake.collideItself():
        snake.respawn()
        #db.snake(snake.coords())

    if not snake.collide(wall):
        snake.respawn()
        #db.snake(snake.coords())
            
    else:
        screen.fill((255,255,255))
        wall.draw(screen)
        apple.draw(screen)
        snake.draw(screen)

    pygame.display.update()
    clock.tick(5)



def quitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
