

class Node:
    def __init__(self, vNumber):
        self.id = vNumber
        self.color = None
        self.edges = []
        self.checked = []
        self.conflictSet = []
        self.painted = []
        self.badEdges = 0
        
    def addEdge(self, edge):
        self.edges.append(edge)
        
    def update(self, color):
        self.color = color
        self.painted.append(color)
        for v in self.edges:
            v.painted.append(color)
            
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
            
    def updateConfSetFromEdge(self, neighbor):
        for v in neighbor.edges:
            if v != self and v not in self.conflictSet:
                self.conflictSet.append(v)
    def getNeighborsColors(self):
        return [ v.color for v in self.edges if v.color != None]
    def canColor(self, color):
        for v in self.edges:
            if v.color != None and v.color == color:
                return False
        return True
    def consis(self):
        if self.color == None:
            return False
        for v in self.edges:
            if v.color == self.color:
                return False
        return True

            