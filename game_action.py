import pygame #is this double import a problem?
import sys

def game_action(apple, clock, db, screen, snake, wall):
    quitCheck()

    #There's also no detection for what is around
    db.saveCheck(snake.checkAround(wall))
    snake.advanceComputer(db.randomMove())

    if snake.collide(apple):
        apple.respawn()
        snake.addLink()
        #db.apple(apple.coords())

    if snake.collideItself():
        snake.respawn()
        db.cleanUp(0.0)
        #db.snake(snake.coords())

    if not snake.collide(wall):
        snake.respawn()
        db.cleanUp(0.0)
        #db.snake(snake.coords())
            
    else:
        db.cleanUp(1.0)
        screen.fill((255,255,255))
        wall.draw(screen)
        apple.draw(screen)
        snake.draw(screen)

    pygame.display.update()
#    clock.tick(5)



def quitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
