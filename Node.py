

class Node:
    def __init__(self, vNumber):
        self.id = vNumber
        self.color = None
        self.edges = []
        self.conflictSet = []
        self.badEdges = 0
        
    def addEdge(self, edge):
        self.edges.append(edge)
        
    def countConstrains(self):
        cons = 0
        self.badEdges = 0
        for v in self.edges:
            if self.color == v.color:
                cons += 1
                self.badEdges += 1
        return cons
    def countBadEdges(self):
        c = 0
        for v in self.edges:
            if self.color == v.color:
                c += 1
        return c
    def updateConflictSet(self):
        for v in self.edges:
            v.conflictSet.append(self)
    def getNeighborsColors(self):
        return [ v.color for v in self.edges if v.color != None]