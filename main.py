




from functions import *
from greedy import Greedy
import copy as cp
from State import State
from feasibilitySearch import feasibilitySearch
from kempeChains import run as runKempe
from backTracking import backTracking
from Hybrid import Hybrid
from forwardChecking import forwardChecking



description = "\n\n==========================================================\n"+"Select algorithm to run:\n"+"Back-tracking with backjumping= 1\nforward-Checking with AC = 2\nfesabile = 3\nKempe chains = 4\nHybrid = 5\n"
inputPath = input("Enter input file path:")
print(description)
algorithm = int(input())
nVertics, nEdges, vertMap, graphDen = parseGraph(inputPath)
print("======================================================================")
print("Initialaizing greedy solution to init initial colors number")
alg = Greedy(cp.deepcopy(list(vertMap.values())))
print("Finished greedy solution with ",alg.numberOfColors,"colors")
print("======================================================================")
res = None
firstState = State(cp.deepcopy(alg.nodes),alg.numberOfColors)
state = State(cp.deepcopy(list(vertMap.values())),alg.numberOfColors)

if algorithm == 1: #Backtracking
    alg = backTracking(state)
    res = alg.run(state,vertMap,firstState)
    
    
elif algorithm == 2: #FC
    alg = forwardChecking(state)  
    res = alg.search(state, cp.deepcopy(vertMap), firstState)
    
elif algorithm == 3:#fesabile
    alg = feasibilitySearch(state,"sim")
    res = alg.search()
    
elif algorithm == 4:#kempe
    res = runKempe(State(alg.nodes, alg.numberOfColors), alg.numberOfColors)
    
    
elif algorithm == 5:#hybrid
    alg = Hybrid(State(alg.nodes, alg.numberOfColors),10000, 5)
    res = alg.search()
    
res.printDetailes()