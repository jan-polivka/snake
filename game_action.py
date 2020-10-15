import pygame #is this double import a problem?
import sys

def game_action(apple, clock, screen, snake, wall):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


    snake.advance()
    #db.addLastMove = snake.lastMove()
    if snake.collide(apple):
        apple.respawn()
        #db.apple() = apple.coords() #This adds a new row

    if not snake.collide(wall):
        snake.respawn()
        #db.cleanUp()
            #Save moves, score, apple positions
            #Add a new row
            
    else:
        screen.fill((255,255,255))
        wall.draw(screen)
        apple.draw(screen)
        snake.draw(screen)

    pygame.display.update()
    clock.tick(30)
