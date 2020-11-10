import random
import math

class DB:
    def __init__(self):
        self.data = [0.0] * 7 #last element is the outcome 0 - dead 1 - alive
        self.dataList = [] 
        self.games = 0


    def addLastMove(self,move):
        dirList = ["left", "right","up","down"]
        self.data[dirList.index(move)] = 1

    def cleanUp(self, result):
        self.data[-1] = float(result)
        self.dataList.append(self.data)
        self.games += 1.0
        self.data = [0] * 7

    def checkDis(self, apple, snake):
         dis = math.sqrt(pow(snake.rect.x - apple.rect.x,2) +
                 pow(snake.rect.y - apple.rect.y,2))
         dis = dis/707 #hypotenuse of a 500 500 quare
         self.data[-3] = float(dis)
         return dis


    def moveValue(self, apple, snake):
        disBefore = math.sqrt(pow(snake.prevX - apple.rect.x,2) + pow(snake.prevY - apple.rect.y,2))
        disAfter = math.sqrt(pow(snake.rect.x - apple.rect.x,2) + pow(snake.rect.y - apple.rect.y,2))
        if (disBefore > disAfter):
            return 1
        elif (disBefore < disAfter):
            return -1
        else:
            return 0

    def randomMove(self):
        dirList = ["left", "right","up","down"]
        choice = random.choice(dirList)
        self.data[-2] = float(dirList.index(choice))
        return choice

    def printDataList(self):
        print (self.dataList)

    def retGames(self):
        return self.games

    def saveCheck(self, detections):
        for mem in range(4):
            self.data[mem] = detections[mem]

    def saveData(self):
        with open('data.txt', 'w') as f:
            for item in self.dataList:
                f.write("%s\n" % item)

    def suggestMove(self, apple, snake):
        dirList = ["left", "right","up","down"]
        disList = [-snake.movX, snake.movX, -snake.movY, snake.movY]
        posList = [0] * 4
        posList[0] = math.sqrt(pow(snake.rect.x+disList[0] - apple.rect.x,2) + pow(snake.rect.y - apple.rect.y,2))
        posList[1] = math.sqrt(pow(snake.rect.x+disList[1] - apple.rect.x,2) + pow(snake.rect.y - apple.rect.y,2))
        posList[2] = math.sqrt(pow(snake.rect.x - apple.rect.x,2) + pow(snake.rect.y+disList[2] - apple.rect.y,2))
        posList[3] = math.sqrt(pow(snake.rect.x - apple.rect.x,2) + pow(snake.rect.y+disList[3] - apple.rect.y,2))
        print (posList[0]) 

        return dirList[posList.index(min(posList))]
