import pygame
from objSnake import Snake
from objApple import Apple
from objWall import Wall
from objDB import DB
from game_action import game_action

import random


def main():

    xAxis, yAxis = 500, 500

    pygame.init()
    screen = pygame.display.set_mode((xAxis,yAxis))


    apple = Apple(275, 275, screen)
    clock = pygame.time.Clock()
    db = DB()
    snake = Snake(50*random.randint(2,6) + 25, 50*random.randint(2,6) + 25, screen)
    db.snake(snake.coords())
    wall = Wall(screen)
    while db.retGames() < 3:
        game_action(apple, clock, db, screen, snake, wall)

    db.printDataList()


if __name__ == "__main__":
    main()
