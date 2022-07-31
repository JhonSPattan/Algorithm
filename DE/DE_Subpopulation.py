from multiprocessing import dummy
from pyclbr import Function
import numpy as np

class DE_Subpopulation():
    def __init__(self,functioneveluate:Function,functionname:str,functiontype:str='Unimodal',populationsize:int=100,subpopulation:int=5,dimension:int=30,round:float=2000,lowerbound:float=-100,upperbound:float=100,cr_fix=True,sf_fix=True) -> None:
        self.functioneveluate = functioneveluate
        self.functioctionname = functionname
        self.functiontype = functiontype
        self.populationsize = populationsize
        self.subpopulation = subpopulation
        self.dimension = dimension
        self.round = round
        self.upperbound = upperbound
        self.lowerbound = lowerbound
        self.cr_fix = cr_fix
        self.sf_fix = sf_fix

    def initialpopulation(self)->np.array:
        population = np.random.uniform(low=self.lowerbound,high=self.upperbound,size=(self.populationsize,self.dimension))
        invers_population = np.array(self.lowerbound+self.upperbound-population)
        combining_population = np.concatenate((population,invers_population))
        fitness_eveluate = np.zeros((self.populationsize,1))
        for i in range(self.populationsize):
            fitness_eveluate[i] = self.functioneveluate(population[i])
    def createsubpopulation(self,population:np.array)->np.array:
        subdimension = self.dimension/self.subpopulation
        col_start = 0
        col_finish = (subdimension-1)
        return_subpopulation = []
        for j in range(subdimension):
            dummy_sub = np.zeros((self.populationsize,subdimension))
            for i in range(self.populationsize):
                dummy_sub[i] = population[i][col_start:col_finish]
            return_subpopulation.append(dummy_sub)
            col_start = col_finish+1
            col_finish = col_finish+subdimension

        return np.array(return_subpopulation)
        


