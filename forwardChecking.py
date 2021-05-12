from Node import Node
from State import State
from functions import *
import copy as cp
from greedy import Greedy
from queue import Queue

class forwardChecking:
    def __init__(self, state):
        self.state = state
        self.colors = state.colors
        self.searchedStates = 0
        
    def MRV(self):
        #All the nodes without colors
        freeNodes = [ (self.state.vertices[i],i) for i in range(len(self.state.vertices)) 
                     if self.state.vertices[i].color == None]
        colors = [i+1 for i in range(self.colors)]
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
        colorsCount = {k:0 for k in [i+1 for i in range(self.colors)]}

        for neighbor in self.state.getNeighbors(current):
            if neighbor.color != None:
                colorsCount[neighbor.color] += 1
        colorsCount = [k for k,v in sorted(colorsCount.items(), key=lambda item: item[1], reverse=False)]
        return colorsCount
    
    
    
    def removeValues(self, edge, domains):
        v2Domain = set()
        #iterate to get v2 colors
        for c in domains[edge[1]]:
            v2Domain.add(c)
        found = False
        if len(v2Domain) == 1:
            color = v2Domain.pop()
            if color in domains[edge[0]]:
                domains[edge[0]].remove(color)
                found = True
            return found
        else:
            return False
    def AC(self, domains):
        edges = Queue()
        for node in self.state.vertices:
            for v in node.edges:
                edges.put((node,v))
        while not edges.empty():
            edge = edges.get()
            if self.removeValues(edge, domains):
                for v in edge[0].edges:
                    edges.put((edge[0],v))
                    
    def backTrackSearch(self, domains):
        emptyNodes = [node for node in self.state.vertices if node.color == None]
        if len(emptyNodes) == 0:
            return self.state
        self.searchedStates += 1
        idx = self.MRV()
        if idx == None:
            return None
        color = self.LCV(self.state.vertices[idx])
        found = False
        newColor = None
        for c in color:
            if self.state.vertices[idx].canColor(c) and found == False:
               self.state.vertices[idx].color, found = c, True
               newColor = c
        if found == False:
            return None
        domains[self.state.vertices[idx]] = [newColor]
        
        self.AC(domains)
        for v in emptyNodes:
            if len(domains[v]) == 0:
                return None
        return self.backTrackSearch(domains)
    
    
    def search(self, state, vertMap,first):
        
        lastSuccess = first
        while True:
            print("Trying with",self.state.colors - 1,"Colors")
            self.__init__(State(cp.deepcopy(list(vertMap.values())),self.state.colors - 1))
            nodes = self.state.vertices
            domains = dict()
            for node in nodes:
                colors = [i+1 for i in range(self.state.colors + 1)]
                domains[node] = colors
            res = self.backTrackSearch(domains)
            if res == None:
                print("\n=========\nSearch stopped, Coloring with",self.state.colors,"Couldnt succeed\n=========")
                return lastSuccess
            else:
                print("success with ",res.colors,"Colors")
                lastSuccess = res
        return None
    

            
