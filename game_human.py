import pygame #is this double import a problem?
import sys

def game_human(apple, clock, db, screen, snake, wall):
    quitCheck()
    
    print (apple.moveValue(snake))

    if not snake.advanceHuman():
        snake.respawn()
    else:
        if snake.collideItself():
            snake.respawn()

    if snake.collide(apple):
        apple.respawn()
        snake.addLink()

    if not snake.collide(wall):
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
