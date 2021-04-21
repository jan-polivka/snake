import pygame #is this double import a problem?
import sys

def game_action(apple, clock, db, screen, snake, wall):
    quitCheck()

    db.saveCheck(snake.checkAround(wall))
    db.checkDis(apple, snake)
    snake.advanceComputer(db.randomMove()) #simple move execution
    #I want to make sure, that the possible collision with itself is recorded
    #in game_human, I make a move, to check collision with the immediate link
    #and then I check collision with the other heads

    if snake.collide(apple):
        db.cleanUp(db.moveValue(apple, snake))
        apple.respawn()
        snake.addLink()

    if snake.collideItself():
        db.cleanUp(-1)
        snake.respawn()

    if not snake.collide(wall):
        db.cleanUp(-1)
        snake.respawn()
            
    else:
        db.cleanUp(db.moveValue(apple, snake))
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
