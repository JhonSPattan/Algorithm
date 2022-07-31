from pyclbr import Function
import pandas as pd
import numpy as np
import csv
import random
from datetime import datetime
#from tqdm import tqdm
main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
#main_path = '/myweb/www/pythonrunnew/Algorithm'
#%% DSIDE Section
class DSIDE_Algorithm():
    def __init__(self,functioneveluate:Function,functionname:str,functiontype:str='UnimodalFunction',dimensiton:int=30,lowerbound:float=-100,upperbound:float=100,round:float=2000,populationsize:int=100,cr_fix:bool=True,sf_fix:bool=True,strategy='DE/rand/1',control:bool=False):
        #self.filename = filename
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
        self.strategy = strategy
        self.control = control

    def build_trial_1(self,r_vector1:np.array,r_vector2:np.array,r_vector3:np.array,target_vector:np.array,crossover_rate:float,scaling_factor:float,alpha:float)->np.array:
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
    
    def build_trial_2(self,r_vector1:np.array,r_vector2:np.array,r_vector3:np.array,r_vector4:np.array,r_vector5:np.array,target_vector:np.array,crossover_rate:float,scaling_factor:float,alpha:float)->np.array:
        dummy_vector = np.random.uniform(low=0,high=1,size=self.dimension)
        trial = np.zeros(self.dimension)
        mutant_vector = alpha*r_vector1+scaling_factor*(r_vector2-r_vector3)+scaling_factor*(r_vector4-r_vector5)
        #print(mutant_vector)
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

    def optimize(self,filename:str,cr_reversed:bool=False,sf_reversed:bool=False,cr:float = 0.8,sf:float = 0.2):
        self.filename = filename
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
        for k in range(replace):
            population = np.zeros((self.populationsize,self.dimension))
            for i in range(self.populationsize):
                dummy = np.random.uniform(low=self.lowerbound,high=self.upperbound+1,size=self.dimension)
                population[i:] = dummy
            now = datetime.now()
            value = np.zeros(self.populationsize)
            for i in range(self.round):
                population_dummy = np.zeros((self.populationsize,self.dimension))
                generation_value = pow(1-(i+1)/self.round,2)
                alpha_value = 1-pow(self.randomvalue,generation_value)
                for j in range(self.populationsize):
                    #print('No control sf and cr')
                    if not self.cr_fix:
                        if fitness_mean == 0:
                            crossover_rate = 0
                        else:
                            crossover_rate = (value[j]-fitness_min)/fitness_mean
                    if not self.sf_fix:
                        #print('Dynamic SF')
                        if fitness_mean == 0:
                            scaling_factor = 0
                        else:
                            scaling_factor = (fitness_max-value[j])/fitness_mean
                    else:
                        if not self.cr_fix:
                            if not cr_reversed:
                                crossover_rate = 0.8-0.3*((i+1)/self.round) #0.8->0.5
                            else:
                                crossover_rate = 0.5+0.3*((i+1)/self.round) #0.5->0.8
                        
                        if not self.sf_fix:
                            #print('SF not fix')
                            if not sf_reversed:
                                scaling_factor = 0.5-0.3*((i+1)/self.round)  #0.5->0.2
                            else:
                                scaling_factor = 0.2+0.3*((i+1)/self.round)  #0.2->0.5
                    
                    
                    vectorrand = np.random.permutation(self.populationsize)
                    #print(vectorrand)
                    if self.strategy == 'DE/rand/1':
                        del_index = np.where(vectorrand == j)[0][0]
                        vectorrand = np.delete(vectorrand,del_index,0)
                        rand_vec1 = population[vectorrand[0]]
                        rand_vec2 = population[vectorrand[1]]
                        rand_vec3 = population[vectorrand[2]]
                        trial_vector = self.build_trial_1(r_vector1=rand_vec1,r_vector2=rand_vec2,r_vector3=rand_vec3,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor,alpha=alpha_value)
                        population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                    elif self.strategy == 'DE/best/1':
                        del_index = np.where(vectorrand == j)[0][0]
                        vectorrand = np.delete(vectorrand,del_index,0)
                        rand_vec1 = population[vectorrand[0]]
                        rand_vec2 = population[vectorrand[1]]
                        trial_vector = self.build_trial_1(r_vector1=minimized_vector,r_vector2=rand_vec1,r_vector3=rand_vec2,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor,alpha=alpha_value)
                        population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                    elif self.strategy == 'DE/rand/2':
                        del_index = np.where(vectorrand == j)[0][0]
                        #print(del_index)
                        vectorrand = np.delete(vectorrand,del_index,0)
                        #print(vectorrand)
                        rand_vec1 = population[vectorrand[0]]
                        rand_vec2 = population[vectorrand[1]]
                        rand_vec3 = population[vectorrand[2]]
                        rand_vec4 = population[vectorrand[3]]
                        rand_vec5 = population[vectorrand[4]]
                        #print(population[vectorrand[0]])
                        trial_vector = self.build_trial_2(r_vector1=rand_vec1,r_vector2=rand_vec2,r_vector3=rand_vec3,r_vector4=rand_vec4,r_vector5=rand_vec5,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor,alpha=alpha_value)
                        population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                    elif self.strategy == 'DE/best/2':
                        del_index = np.where(vectorrand == j)[0][0]
                        vectorrand = np.delete(vectorrand,del_index,0)
                        rand_vec1 = population[vectorrand[0]]
                        rand_vec2 = population[vectorrand[1]]
                        rand_vec3 = population[vectorrand[2]]
                        rand_vec4 = population[vectorrand[3]]
                        trial_vector = self.build_trial_2(r_vector1=minimized_vector,r_vector2=rand_vec1,r_vector3=rand_vec2,r_vector4=rand_vec3,r_vector5=rand_vec4,target_vector=population[j],crossover_rate=crossover_rate,scaling_factor=scaling_factor,alpha=alpha_value)
                        population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                
                for j in range(self.populationsize):
                    population[j] = population_dummy[j]
                    value[j] = self.functioneveluate(population[j])
                
                fitness_max = max(value)
                fitness_min = min(value)
                fitness_mean = np.mean(value)
                
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

        print('Mutant vector strategy: ',self.strategy)
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