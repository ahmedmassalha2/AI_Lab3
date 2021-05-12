
from SimulatedAnnealing import SimulatedAnnealing
from Node import Node
from State import State
from functions import *
from greedy import Greedy

import copy as cp


class Hybrid:
    def __init__(self, state, maxTry, maxEqual):
        self.state = state
        self.maxTry = maxTry 
        self.maxEqual = maxEqual
        self.visited = 0
    
    
    
    def stopCond(self, itr):
        return self.maxTry > itr

    def runKempe(self, state, colors):
        minColor = colors
        bestState = cp.deepcopy(state)
        for color in range(1, colors + 1):
            for swapWith in range(1, colors + 1):
                if color != swapWith:
                    self.visited += 1
                    newState = cp.deepcopy(state)
                    newState.makeSwaps(color, swapWith)
                    
                    if newState.isCons():
                        colors =  self.runKempe(cp.deepcopy(newState), colors - 1)
                        
                        if colors < minColor:
                            minColor = colors
                            bestState = cp.deepcopy(newState)
        return  bestState
    def search(self):
        currObjectiv = self.state.getHypredFitness()
        bestOBJ, bestStateOBJ = currObjectiv, self.state
        i = 0
        tries = self.maxEqual
        while self.stopCond(i):
            newState = cp.deepcopy(bestStateOBJ)
            newState.resetRandomColors()
            newState = self.runKempe(cp.deepcopy(newState),newState.colors)
            newCost = newState.getHypredFitness()
            if newCost < bestOBJ:
                print("Hybird fitnees reduced from",newCost,"to",bestOBJ)
                bestOBJ, bestStateOBJ = newCost, cp.deepcopy(newState)
                bestStateOBJ.updateColors()
                tries = self.maxEqual
                
            else:
                tries -= 1
                if tries == 0:
                    break
            
            i += 1
        bestStateOBJ.visited = self.visited
        return bestStateOBJ


        
