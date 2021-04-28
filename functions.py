from Node import Node
from State import State
# from SimulatedAnnealing import SimulatedAnnealing
# from feasibilitySearch import feasibilitySearch

def parseGraph(path):
    vertMap, nEdges, nVertics =  dict(), 0, 0
    fileGraph = open(path,'r')
    fileGraph = fileGraph.readlines()
    for line in fileGraph:
        if line.startswith('p'):
            data = line.split(' ')
            nVertics = int(data[2])
            nEdges = int(data[3])
        elif line.startswith('e '):
            data = line.split(' ')
            newV, nextV = None, None
            if int(data[1]) not in vertMap.keys():
                newV = Node(int(data[1]))
                vertMap[int(data[1])] = newV
            else:
                newV = vertMap[int(data[1])]
                
            if int(data[2]) not in vertMap.keys():
                nextV = Node(int(data[2]))
                vertMap[int(data[2])] = nextV
            else:
                nextV = vertMap[int(data[2])]
            
            newV.addEdge(nextV)
    
    return nVertics, nEdges, vertMap, (nEdges/(nVertics * (nVertics - 1)))
            
        
# nVertics, nEdges, vertMap = parseGraph('instances/queen8_8.col')
# colors = 500
# state = State(list(vertMap.values()),colors)
# state.resetRandomColors()
# search = feasibilitySearch(state)
# search.search()
# state.resetRandomColors()
# s = SimulatedAnnealing(state, 1000, 100000)
# s.simulate()