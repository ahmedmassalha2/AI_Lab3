from Node import Node
from State import State
from functions import *
import copy as cp
from greedy import Greedy

class backTracking:
    def __init__(self, state):
        self.searchedStates = 0
        self.state = state
        self.colors = []
        for i in range(self.state.colors):
            self.colors.append(i+1)
        
    def resetColors(self):
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
        # print(current)
        colorsCount = {k:0 for k in self.colors}

        for neighbor in self.state.getNeighbors(current):
            if neighbor.color != None:
                colorsCount[neighbor.color] += 1
        colorsCount = [k for k,v in sorted(colorsCount.items(), key=lambda item: item[1], reverse=False)]
        return colorsCount
    
    
    def backTrackSearch(self, idx = None):
        if self.state.isCons() == True:
            return self.state

        if idx == None:
            #This mean we are NOT backjumping
            idx = self.MRV()
            if idx == None:
                return None
        self.searchedStates += 1
        color = self.LCV(self.state.vertices[idx])
        # print(color,self.state.vertices[idx].canColor(color))
        fail = 0
        for c in color:
            if self.state.vertices[idx].canColor(c):
               self.state.vertices[idx].color = c
               self.state.vertices[idx].updateConflictSet()
               if self.backTrackSearch() != None:
                   return self.state
               else:
                   fail += 1
       
        if fail == len(color):
            jumpTo = self.state.getNodeIndex(
                self.state.vertices[idx].conflictSet[
                    len(self.state.vertices[idx].conflictSet) - 1
                    ])
            self.state.vertices[jumpTo].updateConfSetFromEdge(self.state.vertices[idx])
            self.state.vertices[idx].color = None
            self.state.vertices[jumpTo].color = None
            return self.backTrackSearch(jumpTo)
        return None
    def run(self, state, vertMap, firstState):
        
        lastSuccess = firstState
        while True:
            print("Trying with",self.state.colors - 1,"Colors")
            self.__init__(State(cp.deepcopy(list(vertMap.values())),self.state.colors - 1))
            res = self.backTrackSearch()
            if res == None:
                print("\n=========\nSearch stopped, Coloring with",self.state.colors,"Couldnt succeed\n=========")
                return lastSuccess
            else:
                print("success with ",res.colors,"Colors")
                lastSuccess = res
        return None

