from pyclbr import Function
import pandas as pd
import numpy as np
import csv
import random
from datetime import datetime
from tqdm import tqdm
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
main_path = '/home/pythonrunnew/Algorithm'
#main_path = '/myweb/www/pythonrunnew/Algorithm'
#%% DE2N Section
class DE2N_Algorithm():
    def __init__(self,filename:str,functioneveluate:Function,functionname:str,functiontype:str='UnimodalFunction',dimensiton:int=30,lowerbound:float=-100,upperbound:float=100,round:float=2000,populationsize:int=100,cr_fix:bool=True,sf_fix:bool=True):
        self.filename = filename
        self.functioneveluate = functioneveluate
        self.functionname = functionname
        self.functiontype = functiontype
        self.dimension = dimensiton
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.round = round
        self.populationsize = populationsize
        self.cr_fix = cr_fix
        self.sf_fix = sf_fix
        self.main_path = main_path
    #%% Core function
    """ def eveluate(fun:Function,arg:np.array)->float:
        return fun(arg) """

    def selection(self,trial_vector:np.array,target_vector:np.array)->np.array:
        trial_value = self.functioneveluate(trial_vector)
        target_value = self.functioneveluate(target_vector)
        if trial_value <= target_value:
            return trial_vector
        else:
            return target_vector

    #%% DE2N function
    def build_trial_nearest(self,r_vector1:np.array,r_vector2:np.array,target_vector:np.array,crossover_rate:float,scaling_factor:float)->np.array:
        dummy_vector = np.random.uniform(low=0,high=1,size=self.dimension)
        weight = 0.8*crossover_rate
        mutant_vector = weight*target_vector+scaling_factor*(r_vector1-target_vector)+scaling_factor*(r_vector2-target_vector)
        trial = np.zeros(self.dimension)
        for i in range(self.dimension):
            if dummy_vector[i] > crossover_rate:
                trial[i] = target_vector[i]
            else:
                trial[i] = mutant_vector[i]

        for i in range(self.dimension):
            if trial[i] > self.upperbound:
                trial[i] = self.upperbound
            
            elif trial[i] < self.lowerbound:
                trial[i] = self.lowerbound
        
        return trial

    def build_trial_best(self,best_vector:np.array,r_vector1:np.array,target_vector:np.array,crossover_rate:float,scaling_factor:float)->np.array:
        dummy_vector = np.random.uniform(low=0,high=1,size=self.dimension)
        weight = 0.8*crossover_rate
        mutant_vector = weight*best_vector+scaling_factor*(best_vector-target_vector)+scaling_factor*(r_vector1-target_vector)
        trial = np.zeros(self.dimension)
        for i in range(self.dimension):
            if dummy_vector[i] > crossover_rate:
                trial[i] = target_vector[i]
            else:
                trial[i] = mutant_vector[i]

        for i in range(self.dimension):
            if trial[i] > self.upperbound:
                trial[i] = self.upperbound
            elif trial[i] < self.lowerbound:
                trial[i] = self.lowerbound
        return trial

    def distance_index(self,current_vector:np.array,all_vector:np.array)->int:
        distance_value = np.zeros(self.populationsize)
        for i in range(self.populationsize):
            distance_value[i] = np.linalg.norm(current_vector-all_vector[i])
        index_zeros = np.where(distance_value == 0)[0][0]
        dummy_distance = np.delete(distance_value,index_zeros,0)
        return np.where(distance_value == min(dummy_distance))[0][0]

    # Dynamic CR and SF
    def optimize(self,cr_upper:float=0,cr_lower:float=0,sf_upper:float=0,sf_lower:float=0)->None:
        replace = 5
        crossover_rate = cr_upper
        scaling_factor = sf_lower
        minimized_value = 0
        maximized_value = 0
        minuted = 0
        minimized_value_round = np.zeros(self.round)
        minimized_vector = np.zeros(self.dimension)
        minimized_value_keep = np.zeros((self.round,3))
        value_analysis = np.zeros((self.round,3))
        time_perround = np.zeros((replace,1))
        for k in tqdm(range(replace),desc="Function: "+self.functionname+" Experiment: "+self.filename):
            population = np.zeros((self.populationsize,self.dimension))
            for i in range(self.populationsize):
                dummy = np.random.uniform(low=self.lowerbound,high=self.upperbound+1,size=self.dimension)
                population[i:] = dummy
            now = datetime.now()
            for i in range(self.round):
                if not self.cr_fix:
                    crossover_rate = cr_upper-(cr_upper-cr_lower)*((i+1)/self.round)
                if not self.sf_fix:
                    scaling_factor = sf_lower+(sf_upper-sf_lower)*((i+1)/self.round)

                value = np.zeros(self.populationsize)
                population_dummy = np.zeros((self.populationsize,self.dimension))
                for j in range(self.populationsize):
                    value[j] = self.functioneveluate(population[j])

                if i == 0:
                    minimized_value = min(value)
                    index = np.where(value == minimized_value)[0][0]
                    minimized_vector = population[index]

                for j in range(self.populationsize):
                    if value[j] == 0:
                        population_dummy[j] = population[j]
                        continue
                    else:
                        ratio = minimized_value/value[j]
                        if ratio < 0.5:
                            vectorrand = np.random.permutation(self.populationsize)
                            del_index = np.where(vectorrand == j)[0][0]
                            vectorrand = np.delete(vectorrand,del_index,0)
                            rand_vector = population[vectorrand[0]]
                            trial_vector = self.build_trial_best(best_vector=minimized_vector,r_vector1=rand_vector,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor)

                        else:
                            index = self.distance_index(population[j],population)
                            vectorrand = np.random.permutation(self.populationsize)
                            """ del_index = np.where(vectorrand == j)[0][0]
                            vectorrand = np.delete(vectorrand,del_index,0) """
                            del_index = np.where(vectorrand == index)[0][0]
                            vectorrand = np.delete(vectorrand,del_index,0)
                            near_vector = population[index]
                            rand_vector = population[vectorrand[0]]
                            trial_vector = self.build_trial_nearest(r_vector1=near_vector,r_vector2=rand_vector,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor)

                    population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                

                for j in range(self.populationsize):
                    population[j] = population_dummy[j]
                    value[j] = self.functioneveluate(population[j])
                now2 = datetime.now()
                if i == 0:
                    minimized_value = min(value)
                    maximized_value = max(value)
                    minimized_value_round[i] = minimized_value
                    index = np.where(value == minimized_value_round[i])[0][0]
                    minimized_vector = population[index]
                    minuted = (now2-now).seconds
                    min_round = i
                    minimized_value_keep[i][0] = minimized_value
                    minimized_value_keep[i][1] = min_round
                    minimized_value_keep[i][2] = minuted

                    value_analysis[i][0] = maximized_value
                    value_analysis[i][1] = minimized_value
                    value_analysis[i][2] = np.mean(value)
                else:
                    if maximized_value > max(value):
                        maximized_value = max(value)
                    
                    if minimized_value > min(value):
                        minimized_value = min(value)
                        minimized_value_round[i] = minimized_value
                        index = np.where(value == minimized_value_round[i])[0][0]
                        minimized_vector = population[index]
                        minuted = (now2-now).seconds + ((now2-now).microseconds)*1E-6
                        min_round = i
                        minimized_value_keep[i][0] = minimized_value
                        minimized_value_keep[i][1] = min_round
                        minimized_value_keep[i][2] = minuted


                        value_analysis[i][0] = maximized_value
                        value_analysis[i][1] = minimized_value
                        value_analysis[i][2] = np.mean(value)
                    else:
                        minimized_value_round[i] = minimized_value
                        minimized_value_keep[i][0] = minimized_value
                        minimized_value_keep[i][1] = min_round
                        minimized_value_keep[i][2] = minuted

                        value_analysis[i][0] = maximized_value
                        value_analysis[i][1] = minimized_value
                        value_analysis[i][2] = np.mean(value)

            now3 = datetime.now()
            time_perround[k][0] = ((now3-now).seconds+((now3-now).microseconds)*1E-6)/self.round

            file_path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Solution','round','time'])
                writer.writerows(minimized_value_keep)

            """ file_path = self.main_path+'/analysis_result/'+self.functionname+'_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['max','min','mean'])
                writer.writerows(value_analysis) """

        file_path = self.main_path+'/time/'+self.filename+'_timeperround.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time_perround'])
            writer.writerows(time_perround)

        solution = np.zeros((replace,self.round))
        solution_average = np.zeros((1,self.round))
        minsolution = np.zeros(replace)
        timecalculation = np.zeros(replace)
        roundstable = np.zeros(replace)
        
        for k in range(replace):
            path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_'+self.filename+'_run_'+str(k+1)+'.csv'
            my_sol = pd.read_csv(path,nrows=self.round)
            solution[k:] = my_sol['Solution']
            solution[k:] = my_sol['Solution']
            minsolution[k] = min(my_sol['Solution'])
            roundstable[k] = max(my_sol['round'])
            timecalculation[k] = max(my_sol['time'])

        for j in range(self.round):
            for i in range(replace):
                solution_average[0][j] = solution_average[0][j]+(solution[i][j]/replace)
        
        solution_average = np.transpose(solution_average)
        file_path = self.main_path+'/Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Average'])
            writer.writerows(solution_average)

        print('Function: ',self.functionname,' with experiment ',self.filename)
        print('Minimized Solution average: ',np.average(minsolution))
        print('Minimized Solution Max: ',str(max(minsolution)),' Minimized Solution Min: ',str(min(minsolution)))
        print('Minimized Solution standart diviation: ',np.std(minsolution))
        print('Time find optimal solution: ',np.average(timecalculation)/60,' minuted Timeperround ',np.mean(time_perround[0]))
        print('Round find optimal solution: ',np.average(roundstable))
        print('Crossover rate',crossover_rate,'Scaling factor: ',scaling_factor)
        print('=================================================================')

        file_path = self.main_path+'/Graph/logfile/logfile_'+self.functionname+'_'+self.filename+'.txt'
        #file_path = 'C:/Users/patip/Documents/Python/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_'+str(crossover_rate)+'_description_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'.txt'
        f = open(file_path,'a')
        f.write('Minimized Solution average: '+str(np.average(minsolution))+'\n')
        f.write('Minimized Solution Max: '+str(max(minsolution))+'Minimized Solution Min: '+str(min(minsolution))+'\n')
        f.write('Minimized Solution standart diviation: '+str(np.std(minsolution))+'\n')
        f.write('Time find optimal solution: '+str(np.average(timecalculation)/60)+' minuted Timeperround'+str(np.mean(time_perround[0]))+'\n')
        f.write('Round find optimal solution: '+str(np.average(roundstable))+'\n')

                    

#%% DSIDE Section
class DSIDE_Algorithm():
    def __init__(self,filename:str,functioneveluate:Function,functionname:str,functiontype:str='UnimodalFunction',dimensiton:int=30,lowerbound:float=-100,upperbound:float=100,round:float=2000,populationsize:int=100,cr_fix:bool=True,sf_fix:bool=True):
        self.filename = filename
        self.functioneveluate = functioneveluate
        self.functionname = functionname
        self.functiontype = functiontype
        self.dimension = dimensiton
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.round = round
        self.populationsize = populationsize
        self.cr_fix = cr_fix
        self.sf_fix = sf_fix
        self.main_path = main_path
        self.randomvalue = random.uniform(0,1)

    def build_trial(self,r_vector1:np.array,r_vector2:np.array,r_vector3:np.array,target_vector:np.array,crossover_rate:float,scaling_factor:float,alpha:float)->np.array:
        dummy_vector = np.random.uniform(low=0,high=1,size=self.dimension)
        trial = np.zeros(self.dimension)
        mutant_vector = alpha*r_vector1+scaling_factor*(r_vector2-r_vector3)
        for i in range(self.dimension):
            if dummy_vector[i] > crossover_rate:
                trial[i] = target_vector[i]
            else:
                trial[i] = mutant_vector[i]
        
        for i in range(self.dimension):
            if trial[i] > self.upperbound:
                trial[i] = self.upperbound
            elif trial[i] < self.lowerbound:
                trial[i] = self.lowerbound

        return trial
    
    def selection(self,trial_vector:np.array,target_vector:np.array)->np.array:
        trial_value = self.functioneveluate(trial_vector)
        target_value = self.functioneveluate(target_vector)
        if trial_value <= target_value:
            return trial_vector
        else:
            return target_vector

    def optimize(self,cr:float = 0.8,sf:float = 0.2):
        replace = 5
        minimized_value = 0
        maximized_value = 0
        minuted = 0
        minimized_value_round = np.zeros(self.round)
        minimized_vector = np.zeros(self.dimension)
        minimized_value_keep = np.zeros((self.round,3))
        value_analysis = np.zeros((self.round,3))
        time_perround = np.zeros((replace,1))
        crossover_rate = cr
        scaling_factor = sf
        for k in tqdm((range(replace)),desc="Function: "+self.functionname+" Experiment: "+self.filename):
            population = np.zeros((self.populationsize,self.dimension))
            for i in range(self.populationsize):
                dummy = np.random.uniform(low=self.lowerbound,high=self.upperbound+1,size=self.dimension)
                population[i:] = dummy
            now = datetime.now()
            for i in range(self.round):
                population_dummy = np.zeros((self.populationsize,self.dimension))
                value = np.zeros(self.populationsize)
                for j in range(self.populationsize):
                    value[j] = self.functioneveluate(population[j])
                
                fitness_max = max(value)
                fitness_min = min(value)
                fitness_mean = np.mean(value)

                generation_value = pow(1-(i+1)/self.round,2)
                alpha_value = 1-pow(self.randomvalue,generation_value)
                for j in range(self.populationsize):
                    vectorrand = np.random.permutation(self.populationsize)
                    del_index = np.where(vectorrand == j)[0][0]
                    vectorrand = np.delete(vectorrand,del_index,0)
                    rand_vec1 = population[vectorrand[0]]
                    rand_vec2 = population[vectorrand[1]]
                    rand_vec3 = population[vectorrand[2]]
                    if not self.cr_fix:
                        if fitness_mean == 0:
                            crossover_rate = 0
                        else:
                            crossover_rate = (value[j]-fitness_min)/fitness_mean
                    if not self.sf_fix:
                        if fitness_mean == 0:
                            scaling_factor = 0
                        else:
                            scaling_factor = (fitness_max-value[j])/fitness_mean
                    trial_vector = self.build_trial(r_vector1=rand_vec1,r_vector2=rand_vec2,r_vector3=rand_vec3,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor,alpha=alpha_value)
                    population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                for j in range(self.populationsize):
                    population[j] = population_dummy[j]
                    value[j] = self.functioneveluate(population[j])
                now2 = datetime.now()
                if i == 0:
                    minimized_value = min(value)
                    maximized_value = max(value)
                    minimized_value_round[i] = minimized_value
                    index = np.where(value == minimized_value_round[i])[0][0]
                    minimized_vector = population[index]
                    minuted = (now2-now).seconds
                    min_round = i
                    minimized_value_keep[i][0] = minimized_value
                    minimized_value_keep[i][1] = min_round
                    minimized_value_keep[i][2] = minuted
                    
                    #for analys solution
                    value_analysis[i][0] = maximized_value
                    value_analysis[i][1] = minimized_value
                    value_analysis[i][2] = np.mean(value)

                else:
                    if maximized_value > max(value):
                        maximized_value = max(value)

                    if minimized_value > min(value):
                        #count = 0
                        minimized_value = min(value)
                        minimized_value_round[i] = minimized_value
                        index = np.where(value == minimized_value_round[i])[0][0]
                        minimized_vector = population[index]
                        minuted = (now2-now).seconds + ((now2-now).microseconds)*1E-6
                        min_round = i
                        minimized_value_keep[i][0] = minimized_value
                        minimized_value_keep[i][1] = min_round
                        minimized_value_keep[i][2] = minuted


                        value_analysis[i][0] = maximized_value
                        value_analysis[i][1] = minimized_value
                        value_analysis[i][2] = np.mean(value)

                    else:
                        #count = count+1;
                        minimized_value_round[i] = minimized_value
                        minimized_value_keep[i][0] = minimized_value
                        minimized_value_keep[i][1] = min_round
                        minimized_value_keep[i][2] = minuted

                        value_analysis[i][0] = maximized_value
                        value_analysis[i][1] = minimized_value
                        value_analysis[i][2] = np.mean(value)
            
            now3 = datetime.now()
            time_perround[k][0] = ((now3-now).seconds+((now3-now).microseconds)*1E-6)/self.round

            file_path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Solution','round','time'])
                writer.writerows(minimized_value_keep)

        file_path = self.main_path+'/time/'+self.filename+'_timeperround.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time_perround'])
            writer.writerows(time_perround)

        solution = np.zeros((replace,self.round))
        solution_average = np.zeros((1,self.round))
        minsolution = np.zeros(replace)
        timecalculation = np.zeros(replace)
        roundstable = np.zeros(replace)
        
        for k in range(replace):
            path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_'+self.filename+'_run_'+str(k+1)+'.csv'
            my_sol = pd.read_csv(path,nrows=self.round)
            solution[k:] = my_sol['Solution']
            solution[k:] = my_sol['Solution']
            minsolution[k] = min(my_sol['Solution'])
            roundstable[k] = max(my_sol['round'])
            timecalculation[k] = max(my_sol['time'])

        for j in range(self.round):
            for i in range(replace):
                solution_average[0][j] = solution_average[0][j]+(solution[i][j]/replace)
        
        solution_average = np.transpose(solution_average)
        file_path = self.main_path+'/Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Average'])
            writer.writerows(solution_average)

        print('Function: ',self.functionname,' with experiment ',self.filename)
        print('Minimized Solution average: ',np.average(minsolution))
        print('Minimized Solution Max: ',str(max(minsolution)),' Minimized Solution Min: ',str(min(minsolution)))
        print('Minimized Solution standart diviation: ',np.std(minsolution))
        print('Time find optimal solution: ',np.average(timecalculation)/60,' minuted Timeperround ',np.mean(time_perround[0]))
        print('Round find optimal solution: ',np.average(roundstable))
        print('Crossover rate',crossover_rate,'Scaling factor: ',scaling_factor)
        print('=================================================================')

        file_path = self.main_path+'/Graph/logfile/logfile_'+self.functionname+'_'+self.filename+'.txt'
        #file_path = 'C:/Users/patip/Documents/Python/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_'+str(crossover_rate)+'_description_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'.txt'
        f = open(file_path,'a')
        f.write('Minimized Solution average: '+str(np.average(minsolution))+'\n')
        f.write('Minimized Solution Max: '+str(max(minsolution))+'Minimized Solution Min: '+str(min(minsolution))+'\n')
        f.write('Minimized Solution standart diviation: '+str(np.std(minsolution))+'\n')
        f.write('Time find optimal solution: '+str(np.average(timecalculation)/60)+' minuted Timeperround'+str(np.mean(time_perround[0]))+'\n')
        f.write('Round find optimal solution: '+str(np.average(roundstable))+'\n')
                







""" #%% Experimential function
import sys
sys.path.insert(0,main_path)
from Benchmark.functionbenchmark import Sphere as Sphere_fun
from Benchmark.functionbenchmark import Elliptic as Elliptic_fun
from Benchmark.functionbenchmark import Zakharov as Zakharov_fun

from Benchmark.functionbenchmark import HGBat as HGBat_fun
from Benchmark.functionbenchmark import HappyCat as HappyCat_fun
from Benchmark.functionbenchmark import Scaffer2 as Scaffer2_fun

#To input filename:str,functioneveluate:function,functionname:str and functiontype:str='Unimodal',dimensiton:int=30,lowerbound:float=-100,upperbound:float=100,round:float=2000,populationsize:int=100 is config parameter

#%%Experimential-1 Crossover rate fix Sphere
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line1',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line2',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-1line3',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.8)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line4',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2,sf_upper=0.5)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line1',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line2',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-2line3',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.4)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line4',functioneveluate=Sphere_fun,functionname='Sphere',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2,sf_upper=0.5)


#%% Experimential-1 Crossover rate fix Elliptic
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line1',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line2',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-1line3',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.8)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line4',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2,sf_upper=0.5)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line1',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line2',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-2line3',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.4)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line4',functioneveluate=Elliptic_fun,functionname='Elliptic',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2,sf_upper=0.5)

#%% Experimential-1 Crossover rate fix Zakharov

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line1',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line2',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-1line3',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.8)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line4',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2,sf_upper=0.5)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line1',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line2',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-2line3',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.4)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line4',functioneveluate=Zakharov_fun,functionname='Zakharov',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2,sf_upper=0.5)


#%% Experimential-1 Crossover rate fix HGBat
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line1',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line2',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-1line3',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.8)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line4',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2,sf_upper=0.5)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line1',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line2',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-2line3',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.4)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line4',functioneveluate=HGBat_fun,functionname='HGBat',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2,sf_upper=0.5)


#%% Experimential-1 Crossover rate fix HappyCat

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line1',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line2',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-1line3',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.8)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line4',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2,sf_upper=0.5)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line1',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line2',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-2line3',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.4)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line4',functioneveluate=HappyCat_fun,functionname='HappyCat',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2,sf_upper=0.5)
#%% Experimential-1 Crossover rate fix 

# %%Scaffer F6
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line1',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line2',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-1line3',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.8)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-1line4',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2,sf_upper=0.5)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line1',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line2',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DSIDE_Exp1-2line3',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100,sf_fix=False)
DSIDE_obj.optimize(cr=0.4)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp1-2line4',functioneveluate=Scaffer2_fun,functionname='Scaffer2',round=2000,populationsize=100,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.4,sf_lower=0.2,sf_upper=0.5) """
