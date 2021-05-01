

from Node import Node
from State import State
from functions import *
import copy as cp
class backTracking:
    def __init__(self, state):
        self.state = state
        self.colors = []
        for i in range(self.state.colors):
            self.colors.append(i+1)
        
    def MRV(self):
        #All the nodes without colors
        freeNodes = [ (self.state.vertices[i],i) for i in range(len(self.state.vertices)) 
                     if self.state.vertices[i].color == None]
        colors = self.colors
        maxR, mostRistrected = float('inf'), None
        for node in freeNodes:
            #get the colors that can be used
            usedColors = node[0].getNeighborsColors()

            set_difference = set(colors) - set(usedColors)
            canUse = list(set_difference)
            if len(canUse) < maxR:
                maxR = len(canUse)
                mostRistrected = node[1]
        return mostRistrected
    
    
    def LCV(self, current):
        
        
        bestColor, minCount = None, float('inf')
        
        for color in self.colors:
            for v in current.edges:
                cons = 0
                for c in self.colors:
                    if c != colors and not v.canColor(c):
                        cons += 1
                if cons < minCount:
                    minCount, bestColor = cons, color
        return color

    
    
    def backTrackSearch(self, idx = None):
        if self.state.isCons() == True:
            return self.state
        if idx == None:
            #This mean we are NOT backjumping
            idx = self.MRV()
            if idx == None:
                return None
        color = self.LCV(self.state.vertices[idx])

        if self.state.vertices[idx].canColor(color):
           self.state.vertices[idx].color = color
           self.state.vertices[idx].updateConflictSet()
           if self.backTrackSearch() != None:
               
               return self.state

       
        else:
            
            newColor = self.state.getFirstUnusedColor()
            
            if newColor != None and self.state.vertices[idx].canColor(newColor) == True:
                if self.state.vertices[idx].canColor(color):
                   self.state.vertices[idx].color = color
                   self.state.vertices[idx].updateConflictSet()
                   if self.backTrackSearch() != None:
                       
                       return self.state
                
            
            jumpTo = self.state.getNodeIndex(
                self.state.vertices[idx].conflictSet[
                    len(self.state.vertices[idx].conflictSet) - 1
                    ])
            self.state.vertices[jumpTo].updateConfSetFromEdge(self.state.vertices[idx])
            self.state.vertices[idx].color = None
            self.state.vertices[jumpTo].color = None
            return self.backTrackSearch(jumpTo)
                

        return None

nVertics, nEdges, vertMap, graphDen = parseGraph('instances/myGraph.txt')
colors = 3
state = State(list(vertMap.values()),colors)
alg = backTracking(state)
state = alg.backTrackSearch()
print(alg.state.isCons())
colors = set()
for v in state.vertices:
    print('node number', v.id, 'color',v.color)
    colors.add(v.color)
print(colors)
