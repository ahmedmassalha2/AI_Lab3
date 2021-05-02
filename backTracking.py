from Node import Node
from State import State
from functions import *
import copy as cp
from greedy import Greedy
class backTracking:
    def __init__(self, state):
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
        # for v in state.vertices:
        #     print('node number', v.id, 'color',v.color)
        #     for n in v.edges:
        #         print(v.id,n.id)
        if self.state.isCons() == True:
            return self.state

        if idx == None:
            #This mean we are NOT backjumping
            idx = self.MRV()
            if idx == None:
                return None
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
    def run(self, state, vertMap):
        
        lastSuccess = None
        while True:
            self.__init__(State(cp.deepcopy(list(vertMap.values())),self.state.colors - 1))
            res = self.backTrackSearch()
            if res == None:
                return lastSuccess
            else:
                print("success with ",res.colors,"Colors")
                lastSuccess = res
        return None
            


def binarySearchOnColors(state, nVertics):
    low = 1
    high = nVertics
    mid = 0
    lastSuccess = None
    while low < high:
 
        mid = (high + low) // 2
        state.colors = mid
        alg = backTracking(cp.deepcopy(state))
        res = alg.backTrackSearch()
        
        # If x is greater, ignore left half
        if (res == None or not alg.state.isCons()):
            low = mid + 1
            
        else:
            lastSuccess = cp.deepcopy(res)
            high = mid - 1

 
    # If we reach here, then the element was not present
    return lastSuccess

nVertics, nEdges, vertMap, graphDen = parseGraph('instances/inithx.i.1.col')
alg = Greedy(cp.deepcopy(list(vertMap.values())))
print(alg.numberOfColors)
state = State(cp.deepcopy(list(vertMap.values())),alg.numberOfColors)
alg = backTracking(state)
# print(alg.backTrackSearch() == None)
res = alg.run(state,vertMap)
print(res.printDetailes())
