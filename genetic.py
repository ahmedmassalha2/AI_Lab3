from __future__ import division
import time
from random import randint, random, sample, shuffle
import numpy as np
import operator
import re
from functions import *
from State import State
import copy as cp
import copy
GA_ELITRATE = 0.4
maxIterations = 16384
populationSize = 2048
nCitits = 0
class Agent:
    def __init__(self, state, fitness):
        self.state = state
        self.fitness = fitness
        self.age = 0





def initPop(population, buffer,state):
    for i in range(populationSize):
        state.resetRandomColors()
        population.append(Agent(cp.deepcopy(state), 0))
        buffer.append(Agent("", 0))


def getFitness(population):
    Sum=0
    values = []
    for agent in population:
        agent.age+=1     
        agent.fitness = agent.state.fitness()
        values.append(agent.fitness)
    avg = np.mean(values)
    std = np.std(values)
    print("Avarage is: ", avg, "Standard Deviation:", std)



def twoPointCrossOver(population,buffer,esize):
    for i in range(esize, populationSize):
        i1 = randint(0, int(populationSize/2) - 1)
        i2 = randint(0, int(populationSize/2) - 1)       
        buffer[i].string = crossover(population[i1].string,population[i2].string)
    return buffer

    
def elitism(population, buffer, esize):
    return [Agent(x.string, x.fitness) for x in population[:esize]] + [x for x in buffer[esize:]]

def mutate(agent):
    def randomMutation(chromosome_aux):
        chromosome_aux.resetRandomColor()
        return chromosome_aux
        
    def inversion_mutation(chromosome_aux):
            chromosome = agent.string
            
            index1 = randint(0,len(chromosome)-1)
            index2 = randint(index1,len(chromosome)-1)
            
            chromosome_mid = chromosome[index1:index2]
            chromosome_mid.reverse()
            
            chromosome_result = chromosome[0:index1] + chromosome_mid + chromosome[index2:]
            
            return chromosome_result
    def insertion_mutation(chromosome_aux):
            chromosome = agent.string            
            i1, i2 = getTwoIndexesFromState(chromosome)
            chromosome.insert(i2-1,chromosome.pop(chromosome.index(chromosome[i1]))) 
            
            return chromosome
    def swap_mutation(chromosome_aux):
            chromosome = agent.string            
            i1, i2 = getTwoIndexesFromState(chromosome)
            chromosome[i1], chromosome[i2] = chromosome[i2], chromosome[i1]
            
            return chromosome
    agent.state = randomMutation(agent.state)


################################################################
def crossover(parent1, parent2):
        global nCitits

        def simple_random_crossover( chrom1, chrom2):
            child = copy.deepcopy(chrom1)
            sub_route = random_subroute(chrom2)
            for x in sub_route:
                child.pop(child.index(x))
            pos=randint(1,len(chrom1)-1)
            return child[:pos] + sub_route + child[pos:]
        return  simple_random_crossover(parent1, parent1)
def ox(parent1, parent2):
    parent1, parent2 = parent1.vertices ,parent2.vertices
    spos1 = randint(0, int(populationSize) - 1) % len(parent1)
    child = []
    for i in parent1:
        child.append(-1)
    for i in range(len(parent1)):
        if(parent1[i] < len(parent1)/2):
            child[i] = parent1[i]
    k = 0
    for j in range(len(parent1)):
        if parent2[j] >= len(parent1)/2:
            while child[k] != -1:
                k += 1
            child[k] = parent2[j]
    return child
def pmx(parent1,parent2):   
    parent1, parent2 = parent1.vertices ,parent2.vertices
    spos1 = randint(0, int(populationSize) - 1) % len(parent1)
    child = []
    for i in parent1:
        child.append(i)
    for j in range(spos1):
        if parent1[j].color == parent2[spos1].color:
            child[j].color = parent1[spos1].color
            child[spos1].color = parent1[j].color
    return child
    
################################################################
def mate(population, buffer, choiceFunc, crossOverFunc):
    esize = int(populationSize * GA_ELITRATE)
    for i in range(esize):
        buffer[i] = population[i]
    for i in range(esize, populationSize):
        p1,p2 = choiceFunc(population, 25),choiceFunc(population, 25)
        newV = pmx(p1.state, p2.state)

        newState = cp.deepcopy(p1.state)
        newState.vertices = newV
        buffer[i] = Agent(cp.deepcopy(newState), 0)
        buffer[i].age = 0
        # Mate the rest
    
        if random() < GA_MUTATIONRATE:
            mutate(buffer[i])
    return buffer

def tournementSelection(population, size):
    pick1 = population[randint(0,populationSize-1)]     # pick first genom
    for i in range(size):
        pick2 = population[randint(0,populationSize-1)]     # pick second genom

        if pick1.state.fitness() > pick2.state.fitness():   # find better genom
            pick1 = pick2

    return pick1





def aging(population, buffer, size):
    BestAge = 4
    for agent in population:
        agent.fitness += (agent.age-BestAge)**2   # add age bonus
    return RWS(population, buffer, size)
        
    

def startGenetic(path):
    nVertics, nEdges, vertMap, graphDen = parseGraph('instances/myciel3.col')
    state = State(list(vertMap.values()),3)
    
    
    startingTime = time.time()
    clocks = time.process_time()
    population = []
    buffer = []
    
    initPop(population, buffer, state)
    for i in range(maxIterations):
        iterStartingTime = time.time()
        print("ffffffffffff")
        getFitness(population)
        population.sort(key= lambda x: x.fitness)  # sort population array by fitness
        print("Current best state cost: ", population[0].fitness)     # print string with best fitness
        if int(population[0].fitness) == 0:
            print("Elapsed time: ", time.time()-iterStartingTime,"Clock ticks: ",str(time.process_time() - clocks))
            print("")
            return population[0]
        
        buffer = mate(population, buffer, tournementSelection, twoPointCrossOver)  # mate
        population, buffer = buffer, population


            
        print("Elapsed time: ", time.time()-iterStartingTime,"Clock ticks: ",str(time.process_time() - clocks))
        clock = time.process_time()
        print("")


res = startGenetic("E-n33-k4.txt").state
setColors = set()
for v in res.vertices:
    setColors.add(v.color)
print(res.isCons(), setColors)














