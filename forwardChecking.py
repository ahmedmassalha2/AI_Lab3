
from Node import Node
from State import State
from functions import *
import copy as cp
from greedy import Greedy
import random

class forwardChecking:
    def __init__(self, state, colors):
        self.state = state
        self.colors = colors
        self.unPainted = set()
        for node in self.state.vertices:
            self.unPainted.add(node)
        self.allColors = [i for i in range(1,self.colors + 1)]
        
        
    def run(self):
        currentNode = random.randrange(len(self.state.vertices))
        return self.withArcCons(currentNode)
    
    
    def arcConsistinty(self, current, color):
        for node in current.edges:
            available = [c for c in self.allColors 
                         if c != color and c not in node.checked  ]
            if len(available) == 0:
                return False
        return True
    
    
    
    def recursive(self, unPainted, nodes, current = None):
        if current == None:
            current = unPainted[0]
        for color in range(1,self.colors + 1):
            
            if current.canColor(color):
                
                current.color = color
                if current in unPainted:
                    unPainted.remove(current)
                neighbors = [node for node in current.edges if node in unPainted]
                if len(unPainted) == 0:
                    return True
                elif len(neighbors) > 0:
                    for node in neighbors:
                        res = self.recursive(cp.deepCopy(unPainted), cp.deepCopy(nodes), node)
                    
                else:
                    res =  self.recursive(cp.deepCopy(unPainted), cp.deepCopy(nodes))
                    
                
    def withArcCons(self, idx):
        
        
        
        for color in range(1,self.colors + 1):
            if color not in self.state.vertices[idx].checked and self.arcConsistinty(
                    self.state.vertices[idx],color
                    ):
                self.state.vertices[idx].update(color) = color
                if self.state.vertices[idx] in self.unPainted:
                    self.unPainted.remove(self.state.vertices[idx])
                    
                    
                if self.recursive(cp.deepCopy(self.unPainted), cp.deepCopy(self.state.vertices))
                
                
            