import pygame #is this double import a problem?
import sys

def game_action(apple, clock, screen, snake):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


    snake.advance()
    #I might do if they are in proximity
    if snake.coords() == apple.coords():
        apple.respawn()

    screen.fill((0,0,0))
    apple.draw(screen)
    snake.draw(screen)

    pygame.display.update()
    clock.tick(60)
