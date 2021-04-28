
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
    def getNeighbors(self, node):
        neighbors = set()
        for v in self.vertices:
            if node in v.edges:
                for vn in v.edges:
                    neighbors.add(vn)
        if node in neighbors:
            neighbors.remove( node )
        return list( neighbors )
    def isCons(self):
        for node in self.vertices:
            if node.consis() == False:
                return False
        return True
    
    def getNodeIndex(self, v):
        for i in range(len(self.vertices)):
            if v == self.vertices[i]:
                return i
        return None