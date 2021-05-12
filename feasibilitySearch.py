
from SimulatedAnnealing import SimulatedAnnealing
from geneticAlgorithm import geneticAlgorithm
from Node import Node
from State import State
from functions import *
from greedy import Greedy
import copy as cp

class feasibilitySearch:
    def __init__(self, state, algorithm):
        self.state = state
        self.colors = self.state.colors
        self.algorithm = algorithm
        self.searchedStates = 0
        
    

    def search(self):
        color = self.state.colors
        bestf = float('inf')
        newState = None
        while color > 0:
            print("iteration with color",color)
            newState = State(cp.deepcopy(self.state.vertices), color - 1)
            newState.resetRandomColors()
            if self.algorithm == "sim":
                algorithm = SimulatedAnnealing(newState, 1000, 100000,20)
                newState = algorithm.simulate()
                self.searchedStates += algorithm.searchedStates
            else:
                alg = geneticAlgorithm(list(vertMap.values()), alg.numberOfColors)
                newState = alg.run()
            
            
            if newState.fitness() > 0:
                print("\nSearch stopped, Coloring with",color - 1,"Couldnt succeed: ",newState.countBadEdges(),"bad edges\n")
                color = 0
            else:
                self.state = cp.deepcopy(newState)
                color -= 1

            print("finished with colors = ",self.state.colors,"bad edges = ",self.state.countBadEdges())
        return self.state

