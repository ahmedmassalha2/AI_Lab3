
from SimulatedAnnealing import SimulatedAnnealing
from Node import Node
from State import State
from functions import *
from greedy import Greedy
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
            algorithm = SimulatedAnnealing(newState, 1000, 100000,20)
            newState = algorithm.simulate()
            if newState.fitness() > 0:
                color = 0
            else:
                self.state = newState
                color -= 1
            print("finished with colors = ",self.state.colors,"bad edges = ",self.state.countBadEdges())
        
        
# nVertics, nEdges, vertMap, graphDen = parseGraph('instances/le450_15b.col')
# alg = Greedy(list(vertMap.values()))

# state = State(alg.nodes, alg.numberOfColors)
# search = feasibilitySearch(state)
# search.search()
# res = search.binarySearchOnColors(state, nVertics)
# setColors = set()
# for v in res.vertices:
#     setColors.add(v.color)
# print(res.isCons(), setColors)