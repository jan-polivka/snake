import torch

#import pandas as pd

from torch import nn, optim
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
import numpy as np



class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.linOne = nn.Linear(6,25)
        self.linTwo = nn.Linear(25,1)

    def forward(self, x):
        x = self.linOne(x)
        x = F.relu(x)
        x = self.linTwo(x)
        x = F.relu(x)
        return x


def train(myNet, db):

    print ("Training start")
    x = []
    y = []
    for move in db.dataList:
        x.append(move[0:len(move)-1])
        y.append(move[-1])

#    print ("XXXXXXXXXXXXXXX")
#    print(x)
#    print(len(x))
    x = torch.tensor(x)
#    print ("YYYYYYYYYYYYYYY")
#    print(y)
    y = torch.tensor(y)

    RANDOM_SEED = 42
    np.random.seed(RANDOM_SEED)
    torch.manual_seed(RANDOM_SEED)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = RANDOM_SEED)

    myNet = Net() #add data

    criterion = nn.MSELoss()
    optimizer = optim.Adam(myNet.parameters(), lr=0.01)

    for epoch in range(1000):
        y_pred = myNet(x_train) #Here, I give the net training data and it returns predictions

        y_pred = torch.squeeze(y_pred) #what does squeeze mean?
        train_loss = criterion(y_pred, y_train) #Here is the result of the prediction compared to the actual result

        optimizer.zero_grad() #what does this do?
        train_loss.backward() #self-explanatory but how?
        optimizer.step() #I guess this just optimizes onces? check if true

    MODEL_PATH = 'model.pth'
    torch.save(myNet, MODEL_PATH)
    #myNet = torch.load(MODEL_PATH)
    print ("Training finish")


def predict(myNet, data):
    print (data)
    t = torch.as_tensor(data).float()
    output = myNet(t)
#    print (output.item())
#    print (round(output.item()) == 1.0)
    if round(output.item()) == 1.0:
        return True
    else:
        return False
