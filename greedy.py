from functions import *

class Greedy:
    def __init__(self, nodes):
        self.nodes = nodes
        self.numberOfColors= 0
        self.run()
        
        
    def run(self):
        colorsNumber = 0
        colors = []
        
        for node in self.nodes:
            currentColors = [v.color for v in node.edges if v != None]
            if len(list(set(colors) - set(currentColors))) == 0:
                colorsNumber += 1
                colors.append(colorsNumber)
            node.color = list(set(colors) - set(currentColors))[0]
        self.numberOfColors = colorsNumber
            
nVertics, nEdges, vertMap, graphDen = parseGraph('instances/inithx.i.1.col')

# alg = Greedy(list(vertMap.values()))
# print(alg.numberOfColors)