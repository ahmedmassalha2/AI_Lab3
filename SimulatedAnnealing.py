from time import time
import copy as cp
from random import randrange, uniform
import numpy as np
class SimulatedAnnealing:
    def __init__(self, state, initTemp, maxIter, maxTime = 40):
        self.state = state
        self.initTemp = initTemp
        self.maxIter = maxIter
        self.maxTime = maxTime
        
        
    def simulate(self):
        startTime = time()
        self.nColors = self.state.colors
        temp = self.initTemp
        for iteration in range(self.maxIter):
            for j in range(100):
                cost = self.state.fitness()
                
                if cost == 0 or time() - startTime > self.maxTime:
                    return self.state
                nextState = self.getNeighbor()
                cost_diff = nextState.fitness() - cost
                if cost_diff < 0:
                    self.state = nextState
                    
                else:
                    try:
                        ans = np.exp(-cost_diff / temp)
        
                    except OverflowError:
                        ans = float('inf')
                        if uniform(0, 1) < ans:
                            self.state = nextState
            temp = temp * 0.95
            cost = self.state.fitness()
            print("current cost",self.state.fitness(), "number of colors:",self.nColors)
            if cost == 0 or time() - startTime > self.maxTime:
                return self.state
        
        return self.state
    
    
    def getNeighbor(self):
        neighbor = cp.deepcopy(self.state)
        randomNodeIDX = randrange(len(self.state.vertices))
        randomColor = randrange(self.nColors)
        neighbor.vertices[randomNodeIDX].color = randomColor
        return neighbor
        