import pygame
from objSnake import Snake
from objApple import Apple
from game_action import game_action


def main():

    xAxis, yAxis = 500, 500

    pygame.init()
    screen = pygame.display.set_mode((xAxis,yAxis))


    apple = Apple(20,20)
    clock = pygame.time.Clock()
    snake = Snake(0,0)
    while 1:
        game_action(apple, clock, screen, snake)


if __name__ == "__main__":
    main()
