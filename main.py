import pygame
from objSnake import Snake
from objApple import Apple
from objWall import Wall
from game_action import game_action


def main():

    xAxis, yAxis = 500, 500

    pygame.init()
    screen = pygame.display.set_mode((xAxis,yAxis))


    apple = Apple(275, 275, screen)
    clock = pygame.time.Clock()
    snake = Snake(25, 25, screen)
    wall = Wall(screen)
    while 1:
        game_action(apple, clock, screen, snake, wall)


if __name__ == "__main__":
    main()
