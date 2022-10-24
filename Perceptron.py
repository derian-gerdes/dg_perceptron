"""
Takes a three column csv file as input as creates a line that separates
the two sets of data. Column 1 is the x value, column 2 is the y value, column
3 is 1 or -1, which is the value that distinguishes one type from another.
"""

import random
from typing import Counter

class Perceptron:
    def __init__(self):
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.x = None
        self.y = None
        self.truth = None
        self.bias = 1


    def loadData(self, filename):
        f = open(filename, "r") 
        xList = []
        yList = []
        truthList = []
        for line in f:
            currentline = line.strip().split(",")
            xList.append(float(currentline[0]))
            yList.append(float(currentline[1]))
            truthList.append(float(currentline[2]))
    

        self.x = xList
        self.y = yList
        self.truth = truthList

    def trainPerceptron(self):
        count = 10
        passes = 0
        errors = 100
        #for i in range(2000):
        while errors > 13:
            count = 0
            passes += 1  
            errors = 0          
            self.shuffleSet()
            for i in range(len(self.x)):
                modelFct = self.c1*self.bias + self.c2*self.x[i] + self.c3*self.y[i]
                if self.truth[i] == -1 and modelFct >= 0:
                    self.c1 = self.c1 - self.bias
                    self.c2 = self.c2 - self.x[i]
                    self.c3 = self.c3 - self.y[i]
                    count += 1
                elif self.truth[i] == 1 and modelFct <= 0:
                    self.c1 = self.c1 + self.bias
                    self.c2 = self.c2 + self.x[i]
                    self.c3 = self.c3 + self.y[i]
                    count += 1
            errors = self.evalSol()
            
        print("The number of passes required were", passes)

    def printResults(self):
        print(self.c1, " + ", self.c2, "*x", " + ", self.c3, "*y")
        print("c1 =", self.c1, "/ c2 =", self.c2, "/ c3 =", self.c3)
    
    def shuffleSet(self):
        ord = []
        myx = []
        myy = []
        myt = []
        for i in range(len(self.x)):
            ord.append(i)
        random.shuffle(ord)
        for i in ord:
            myx.append(self.x[ord[i]])
            myy.append(self.y[ord[i]])
            myt.append(self.truth[ord[i]])
        self.x = myx
        self.y = myy
        self.truth = myt

    def evalSol(self):
        count = 0
        for i in range(len(self.truth)):
            modelFct = self.c1*self.bias + self.c2*self.x[i] + self.c3*self.y[i]
            if self.truth[i] == -1 and modelFct >= 0:
                count += 1
            elif self.truth[i] == 1 and modelFct <= 0:
                count += 1
        return count



def main():
    p = Perceptron()
    #p.loadData("yourfile.csv")
    p.trainPerceptron()
    p.printResults()
    print("The number of errors were", p.evalSol())

main()


