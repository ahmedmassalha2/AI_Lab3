

from Node import Node
from State import State
from functions import *
import copy as cp
import random


import os

from greedy import Greedy
import csv
import time
def run(state, colors):
        visited = 0
        minColor = colors
        bestState = cp.deepcopy(state)
        for color in range(1, colors + 1):
            for swapWith in range(1, colors + 1):
                if color != swapWith:
                    visited += 1
                    newState = cp.deepcopy(state)
                    newState.makeSwaps(color, swapWith)
                    
                    if newState.kempeOBJ() > state.kempeOBJ() and newState.isCons():
                        colors, newState =  run(cp.deepcopy(newState), colors - 1)
                        
                        if colors < minColor:
                            minColor = colors
                            bestState = cp.deepcopy(newState)
        bestState.visited = visited
        return  bestState
