from random import randrange, randint, random
from Node import Node
import copy as cp
import numpy as np
from time import time
from functions import *
from greedy import Greedy
class Agent:
    def __init__(self, state, fitness):
        self.nodes = state
        self.fitness = fitness
        self.age = 0
        
    def updateFitness(self):
        fitness = 0
        for node in self.nodes:
            fitness += node.countConstrains()
        self.fitness = fitness
        
        
class geneticAlgorithm:
    def __init__(self, nodes, colors, GA_ELITRATE = 0.4, maxIterations = 16384, 
                 populationSize = 2048, GA_MUTATIONRATE = 0.25):
        self.GA_ELITRATE, self.maxIterations, self.populationSize, self.GA_MUTATIONRATE = GA_ELITRATE, maxIterations, populationSize, GA_MUTATIONRATE
        self.population, self.nodes, self.colors = [], nodes, colors
        self.avg, self.std = 0, 0
        print("initializing population with", colors,"colors")
        self.initPop()
        print("finish init")
        
        
        
    def initPop(self):
        for i in range(self.populationSize):
            newAgentNodes = cp.deepcopy(self.nodes)
            for node in newAgentNodes:
                node.color = randrange(self.colors) + 1
            self.population.append(Agent(newAgentNodes, 0))
    def calcitness(self):
        values = []
        for agent in self.population:
            agent.updateFitness()
            values.append(agent.fitness)
        self.avg, self.std = np.mean(values), np.std(values)
        self.population.sort(key= lambda x: x.fitness)
            
    
    def getParents(self, size):
        pick1 = self.population[randint(0,self.populationSize-1)]     # pick first genom
        for i in range(size):
            pick2 = self.population[randint(0,self.populationSize-1)]     # pick second genom
    
            if pick1.fitness > pick2.fitness:   # find better genom
                pick1 = pick2
    
        return pick1
    
    
    def crossOver(self, p1, p2):
        spos1 = randint(0, len(p1.nodes) - 2)
        spos2 = randint(spos1+1, len(p1.nodes) - 1)
       
        return  cp.deepcopy(p1.nodes[:spos1] + p2.nodes[spos1:spos2]+ p1.nodes[spos2:])
    
    
    def mutate(self, nodes):
        for v in nodes:
            found = False
            for nei in v.edges:
                if v.color == nei.color and found == False:
                    v.color = randrange(self.colors) + 1
                    found = True
        return nodes
    def mating(self):
        buffer = self.population[:int(self.populationSize * self.GA_ELITRATE)]
        
        while len(buffer) < self.populationSize:
            p1, p2 = self.getParents(25), self.getParents(25)
            newAgent = self.crossOver(p1, p2)
            if random() < self.GA_MUTATIONRATE:
                newAgent = self.mutate(newAgent)
            buffer.append(Agent(newAgent, 0))
        self.population = buffer
    
    
    def run(self):
        startTime = time()
        
        self.calcitness()
        for i in range(self.maxIterations):
            self.mating()
            self.calcitness()
            
            elapsedTime = time() - startTime
            
            print("Total cost: ", self.population[0].fitness, "Total time: ", elapsedTime)
            if(self.population[0].fitness == 0):
                return self.population[0]
            startTime = time()
