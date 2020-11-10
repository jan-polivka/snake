import pygame
from objSnake import Snake
from objApple import Apple
from objWall import Wall
from objDB import DB
from game_action import game_action
from model_apple import Net, predict, train
from game_predict import game_predict

import random


def main():

    xAxis, yAxis = 500, 500

    pygame.init()
    screen = pygame.display.set_mode((xAxis,yAxis))


    apple = Apple(275, 275, screen)
    clock = pygame.time.Clock()
    db = DB()
    snake = Snake(50*random.randint(2,6) + 25, 50*random.randint(2,6) + 25, screen)
#    db.snake(snake.coords())
    wall = Wall(screen)
    while db.retGames() < 200:
        game_action(apple, clock, db, screen, snake, wall)

#    db.printDataList()
    db.saveData()

    data = []
    #with open('data.txt','r') as f:
        #for item in my_list:
            #f.write("%s\n" % item)

    #train?
    myNet = Net()
    train(myNet, db)

    while 1:
        game_predict(apple, clock, db, myNet, screen, snake, wall)

    #predict(myNet, [0,1,1,0,0])

    #train.predict(myNet, [1,0,1,0,0])
    #train.predict(myNet, [0,0,1,0,1])
    #train.predict(myNet, [1,0,1,0,2])


if __name__ == "__main__":
    main()
