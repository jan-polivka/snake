import pygame #is this double import a problem?
import sys

def game_action(apple, clock, db, screen, snake, wall):
    quitCheck()

    db.saveCheck(snake.checkAround(wall))
    db.checkDis(apple, snake)
    snake.advanceComputer(db.randomMove())

    if snake.collide(apple):
        db.cleanUp(db.moveValue(apple, snake)+1)
        apple.respawn()
        snake.addLink()

    if snake.collideItself():
        db.cleanUp(db.moveValue(apple, snake))
        snake.respawn()

    if not snake.collide(wall):
        db.cleanUp(db.moveValue(apple, snake))
        snake.respawn()
            
    else:
        db.cleanUp(db.moveValue(apple, snake)+1)
        screen.fill((255,255,255))
        wall.draw(screen)
        apple.draw(screen)
        snake.draw(screen)

    pygame.display.update()
#    clock.tick(10)



def quitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
