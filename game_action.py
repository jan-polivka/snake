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
#    apple.coords()
#    snake.coords()
    #I might do if they are in proximity
#    if snake.coords() == apple.coords():
#        apple.respawn()

    if snake.collide(apple):
        apple.respawn()
        snake.addLink()

    if snake.collideItself():
        snake.respawn()

    if not snake.collide(wall):
        snake.respawn()
    else:
        screen.fill((255,255,255))
        wall.draw(screen)
        apple.draw(screen)
        snake.draw(screen)

    pygame.display.update()
    clock.tick(5)
