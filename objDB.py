import random

class DB:
    def __init__(self):
#        self.data = {"start":None, "apple":[], "moves":[]}
        #self.data = {"left":, "right":,"up":,"down":, "sugg":}
        self.data = [0.0] * 6 #last element is the outcome 0 - dead 1 - alive
        self.dataList = [] 
        self.games = 0


    def addLastMove(self,move):
        dirList = ["left", "right","up","down"]
        self.data[dirList.index(move)] = 1

#    def apple(self, coords):
#        self.data['apple'].append(coords)

    def cleanUp(self, result):
        self.data[-1] = float(result)
        self.dataList.append(self.data)
        self.games += 1.0
        self.data = [0] * 6

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
            #f.write(str(self.dataList))
            for item in self.dataList:
                f.write("%s\n" % item)

#    def snake(self, coords):
#        self.data['start'] = coords

