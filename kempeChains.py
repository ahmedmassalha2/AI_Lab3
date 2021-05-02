

from Node import Node
from State import State
from functions import *
import copy as cp
from greedy import Greedy
import random

class kempeChains:
    def __init__(self, state):
        
        self.state, self.colors = state, state.colors
        
    def run(self, state):
        print("hhhhhhhhhh")
        minColor = state.colors
        for color in range(1, state.colors + 1):
            for swapWith in range(1, state.colors + 1):
                if color != swapWith:
                    state.makeSwaps(color, swapWith)
                    if state.isCons():
                        newState = cp.deepCopy(state)
                        newState.colors = state.colors - 1
                        colors =  self.run(newState)
                        if colors < minColor:
                            minColor = colors
        return  minColor

def run(state, colors):
        print("hhhhhhhhhh")
        minColor = colors
        for color in range(1, colors + 1):
            for swapWith in range(1, colors + 1):
                if color != swapWith:
                    state.makeSwaps(color, swapWith)
                    if state.isCons():
                        print("aaa")
                        newState = cp.deepCopy(state)
                        colors =  run(newState, colors - 1)
                        if colors < minColor:
                            minColor = colors
        return  minColor
nVertics, nEdges, vertMap, graphDen = parseGraph('instances/le450_15b.col')
       
alg = Greedy(list(vertMap.values()))
print(alg.numberOfColors)
state = State(alg.nodes, alg.numberOfColors)
alg = run(state, alg.numberOfColors)
