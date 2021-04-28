
from random import randrange

class State:
    
    def __init__(self,state, colors):
        self.vertices = state
        self.colors = colors
    
    def fitness(self):
        fitness = 0
        for node in self.vertices:
            fitness += node.countConstrains()
        return fitness
    
    def countBadEdges(self):
        badEdges = 0
        for node in self.vertices:
            badEdges += node.countBadEdges()
        return badEdges
    def resetRandomColors(self):
        for v in self.vertices:
            v.color = randrange(self.colors) + 1