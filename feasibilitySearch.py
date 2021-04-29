
from SimulatedAnnealing import SimulatedAnnealing
from Node import Node
from State import State
from functions import *
import copy as cp
class feasibilitySearch:
    def __init__(self, state):
        self.state = state
        self.colors = self.state.colors
        
    
    
    def search(self):
        color = self.state.colors
        while color > 0:
            print("iteration with color",color)
            newState = State(cp.deepcopy(self.state.vertices), color - 1)
            newState.resetRandomColors()
            algorithm = SimulatedAnnealing(newState, 1000, 100000,3)
            newState = algorithm.simulate()
            if newState.fitness() > 0:
                color = 0
            else:
                self.state = newState
                color -= 1
            print("finished with colors = ",self.state.colors,"bad edges = ",self.state.countBadEdges())
        
        
nVertics, nEdges, vertMap, graphDen = parseGraph('instances/le450_5a.col')
colors =5
state = State(list(vertMap.values()),colors)
state.resetRandomColors()
search = feasibilitySearch(state)
search.search()