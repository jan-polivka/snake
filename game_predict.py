import pygame #is this double import a problem?
import sys

from model_apple import predict

import random

import copy

def game_predict(apple, clock, db, net, screen, snake, wall):
    quitCheck()

    state = snake.checkAround(wall)
    dirList = ["left","right","up","down"]
    selecting = True
    randSel = 0
    state.append(db.checkDis(apple, snake))
    state.append(randSel)
    #what is this thing?
    #I know!
    #It cycles through possible directions to find one that
    #we should take by predict return 1
    while selecting == True:
        randSel = random.randint(0,3)
        state[-1] = randSel
        move = predict(net, state)
        if not move:
            selecting = False

    snake.advanceComputer(dirList[randSel])

    if snake.collide(apple):
        apple.respawn()
        snake.addLink()

    if snake.collideItself():
#        print (state)
        print ("dead")
        snake.respawn()

    if not snake.collide(wall):
#        print (state)
        print ("dead")
        snake.respawn()
            
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
