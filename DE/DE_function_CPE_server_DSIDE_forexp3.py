from pyclbr import Function
import numpy as np
import pandas as pd
import csv
import random
import os
from datetime import datetime

#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'

class DSIDE_Algorithm():
    def __init__(self,functioneveluate:Function,functionname:str,functiontype:str='UnimodalFunction',dimensiton:int=30,lowerbound:float=-100,upperbound:float=100,round:float=2000,populationsize:int=100,strategy='DE/rand/1',equlationoption='switch_compare'):
        self.functioneveluate = functioneveluate
        self.functionname = functionname
        self.functiontype = functiontype
        self.dimension = dimensiton
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.round = round
        self.populationsize = populationsize
        self.main_path = main_path
        self.randomvalue = random.uniform(0,1)
        self.strategy = strategy
        self.equlationoption = equlationoption


    def build_trial_vaector(self,r_vector1:np.array,r_vector2:np.array,r_vector3:np.array,target_vector:np.array,crossover_rate:float,scaling_factor:float,alpha:float)->tuple:
        component = np.array([r_vector1,r_vector2,r_vector3])
        dummy_vector = np.random.uniform(low=0,high=1,size=self.dimension)
        trial = np.zeros(self.dimension)
        d_trial1 = np.zeros(self.dimension)
        d_trial2 = np.zeros(self.dimension)
        crossover_1_count = 0
        crossover_2_count = 0
        dimension_count = 0
        if self.equlationoption == 'switch_compare':
            mutant_vector1 = alpha*component[0]+scaling_factor*(component[1]-component[2])
            mutant_vector2 = alpha*component[0]+scaling_factor*(component[2]-component[1])
            
        elif self.equlationoption == 'random_compare':
            vectorrand = np.random.permutation(3)
            mutant_vector1 = alpha*component[0]+scaling_factor*(component[1]-component[2])
            mutant_vector2 = alpha*component[vectorrand[0]]+scaling_factor*(component[vectorrand[1]]-component[vectorrand[2]])

        for i in range(self.dimension):
                if dummy_vector[i] > crossover_rate:
                    d_trial1[i] = target_vector[i]
                else:
                    d_trial1[i] = mutant_vector1[i]
                    crossover_1_count = crossover_1_count+1

        for i in range(self.dimension):
                if dummy_vector[i] > crossover_rate:
                    d_trial2[i] = target_vector[i]
                else:
                    d_trial2[i] = mutant_vector2[i]
                    crossover_2_count = crossover_2_count+1

        trial = self.selection(d_trial1,d_trial2)
        if (trial == d_trial1).all():
            dimension_count = crossover_1_count
        else:
            dimension_count = crossover_2_count
        
        return trial,dimension_count
    
    def selection(self,trial_vector:np.array,target_vector:np.array)->np.array:
        trial_value = self.functioneveluate(trial_vector)
        target_value = self.functioneveluate(target_vector)
        if trial_value <= target_value:
            return trial_vector
        else:
            return target_vector

    def optimize(self,filename:str,cr:float = 0.8,sf:float = 0.2):
        self.filename = filename
        self.crossovercount = np.zeros((self.round,3))
        replace = 5

        minimized_value = 0
        maximized_value = 0
        minuted = 0
        minimized_value_round = np.zeros(self.round)
        minimized_vector = np.zeros(self.dimension)
        minimized_value_keep = np.zeros((self.round,3))
        value_analysis = np.zeros((self.round,3))
        time_perround = np.zeros((replace,1))

        crossoverrateValuedata = np.zeros((self.round,3))
        crossoverrateInpopulation = np.zeros(self.populationsize)

        scalingfactorValuedata = np.zeros((self.round,3))
        scalingfactorInpopulation = np.zeros(self.populationsize)

        dimensionChangecount = np.zeros((self.round,3))
        dimensionChangeinpopulation = np.zeros(self.populationsize)


        crossoverRate = cr
        scalingFactor = sf
        for k in range(replace):
            population = np.zeros((self.populationsize,self.dimension))
            acceptCountinpopulation = np.zeros((self.round,1))
            for i in range(self.populationsize):
                population[i:] = np.random.uniform(low=self.lowerbound,high=self.upperbound+1,size=self.dimension)
            now = datetime.now()
            value = np.zeros(self.populationsize)
            for j in range(self.populationsize):
                value[j] = self.functioneveluate(population[j])
            fitness_max = max(value)
            fitness_min = min(value)
            fitness_mean = np.mean(value)
            index = np.where(value == fitness_min)[0][0]
            minimized_vector = population[index]
            for i in range(self.round):
                population_dummy = np.zeros((self.populationsize,self.dimension))
                generation_value = pow(1-(i+1)/self.round,2)
                alpha_value = 1-pow(self.randomvalue,generation_value)
                for j in range(self.populationsize):
                    if fitness_mean == 0:
                        crossoverRate = 0
                    else:
                        crossoverRate = (value[j]-fitness_min)/fitness_mean
                    crossoverrateInpopulation[j] = crossoverRate
                    
                    if fitness_mean == 0:
                        scalingFactor = 0
                    else:
                        scalingFactor = (fitness_max-value[j])/fitness_mean
                    scalingfactorInpopulation[j] = scalingFactor

                    vectorrand = np.random.permutation(self.populationsize)
                    if self.strategy == 'DE/rand/1':
                        del_index = np.where(vectorrand == j)[0][0]
                        vectorrand = np.delete(vectorrand,del_index,0)
                        rand_vec1 = population[vectorrand[0]]
                        rand_vec2 = population[vectorrand[1]]
                        rand_vec3 = population[vectorrand[3]]
                        trial_vector,dimensionChangeinpopulation[j] = self.build_trial_vaector(r_vector1=rand_vec1,r_vector2=rand_vec2,r_vector3=rand_vec3,target_vector=population[j],crossover_rate=crossoverRate,scaling_factor=scalingFactor,alpha=alpha_value)
                        population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                        if (population_dummy[j] == trial_vector).all():
                            #print('accept')
                            acceptCountinpopulation[i][0] = acceptCountinpopulation[i][0]+1
                    elif self.strategy == 'DE/best/1':
                        del_index = np.where(vectorrand == j)[0][0]
                        vectorrand = np.delete(vectorrand,del_index,0)
                        rand_vec1 = minimized_vector
                        rand_vec2 = population[vectorrand[0]]
                        rand_vec3 = population[vectorrand[1]]
                        trial_vector,dimensionChangeinpopulation[j] = self.build_trial_vaector(r_vector1=rand_vec1,r_vector2=rand_vec2,r_vector3=rand_vec3,target_vector=population[j],crossover_rate=crossoverRate,scaling_factor=scalingFactor,alpha=alpha_value)
                        population_dummy[j] = self.selection(trial_vector=trial_vector,target_vector=population[j])
                        if (population_dummy[j] == trial_vector).all():
                            acceptCountinpopulation[i][0] = acceptCountinpopulation[i][0]+1

                
                crossoverrateValuedata[i][0] = np.max(crossoverrateInpopulation)
                crossoverrateValuedata[i][1] = np.min(crossoverrateInpopulation)
                crossoverrateValuedata[i][2] = np.mean(crossoverrateInpopulation)

                scalingfactorValuedata[i][0] = np.max(scalingfactorInpopulation)
                scalingfactorValuedata[i][1] = np.min(scalingfactorInpopulation)
                scalingfactorValuedata[i][2] = np.mean(scalingfactorInpopulation)

                dimensionChangecount[i][0] = np.max(dimensionChangeinpopulation)
                dimensionChangecount[i][1] = np.min(dimensionChangeinpopulation)
                dimensionChangecount[i][2] = np.mean(dimensionChangeinpopulation)
        
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

            file_path = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_crossovervalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Max','Min','Mean'])
                writer.writerows(crossoverrateValuedata)

            file_path = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_scalingvalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Max','Min','Mean'])
                writer.writerows(scalingfactorValuedata)

            file_path = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_dimensionvalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Max','Min','Mean'])
                writer.writerows(dimensionChangecount)

            #print(acceptCountinpopulation)
            #acceptCountinpopulation = np.transpose(acceptCountinpopulation)
            file_path = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_acceptvalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Accept'])
                for jk in range(self.round):
                    writer.writerow([acceptCountinpopulation[i][0]])
        
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
            minsolution[k] = min(my_sol['Solution'])
            roundstable[k] = max(my_sol['round'])
            timecalculation[k] = max(my_sol['time'])
            os.remove(path=path)


        for j in range(self.round):
            for i in range(replace):
                solution_average[0][j] = solution_average[0][j]+(solution[i][j]/replace)
        
        solution_average = np.transpose(solution_average)
        file_path = self.main_path+'/Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Average'])
            writer.writerows(solution_average)

        scalingfactorAnalysismax = np.zeros((replace,self.round))
        scalingfactorAnalysismin = np.zeros((replace,self.round))
        scalingfactorAnalysismean = np.zeros((replace,self.round))

        crossoverAnalysismax = np.zeros((replace,self.round))
        crossoverAnalysismin = np.zeros((replace,self.round))
        crossoverAnalysismean = np.zeros((replace,self.round))

        dimensionAnalysismax = np.zeros((replace,self.round))
        dimensionAnalysismin = np.zeros((replace,self.round))
        dimensionAnalysismean = np.zeros((replace,self.round))

        acceptAnalysis = np.zeros((replace,self.round))

        scalingfactorAveragevalue = np.zeros((self.round,3))
        crossoverAveragevalue = np.zeros((self.round,3))
        dimensionAverage = np.zeros((self.round,3))
        acceptAverage = np.zeros(self.round)
        
        for k in range(replace):
            scalingpath = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_scalingvalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            scalingsol = pd.read_csv(scalingpath,nrows=self.round)
            scalingfactorAnalysismax[k:] = scalingsol['Max']
            scalingfactorAnalysismin[k:] = scalingsol['Min']
            scalingfactorAnalysismean[k:] = scalingsol['Mean']

            crossoverpath = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_crossovervalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            crossoversol = pd.read_csv(crossoverpath,nrows=self.round)
            crossoverAnalysismax[k:] = crossoversol['Max']
            crossoverAnalysismin[k:] = crossoversol['Min']
            crossoverAnalysismean[k:] = crossoversol['Mean']

            dimensionpath = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_dimensionvalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            dimensionsol = pd.read_csv(dimensionpath)
            dimensionAnalysismax[k:] = dimensionsol['Max']
            dimensionAnalysismin[k:] = dimensionsol['Min']
            dimensionAnalysismean[k:] = dimensionsol['Mean']

            acceptpath = self.main_path+'/scaling_result/'+self.functionname+'_result/'+self.functionname+'_acceptvalue_'+self.filename+'_run_'+str(k+1)+'.csv'
            acceptsol  = pd.read_csv(acceptpath)
            acceptAnalysis[k:] = acceptsol['Accept']

            os.remove(path = scalingpath)
            os.remove(path = crossoverpath)
            os.remove(path = dimensionpath)
            os.remove(path = acceptpath)

        for j in range(self.round):
            for i in range(replace):
                scalingfactorAveragevalue[j][0] = scalingfactorAveragevalue[j][0] + (scalingfactorAnalysismax[i][j]/replace)
                scalingfactorAveragevalue[j][1] = scalingfactorAveragevalue[j][1] + (scalingfactorAnalysismin[i][j]/replace)
                scalingfactorAveragevalue[j][2] = scalingfactorAveragevalue[j][2] + (scalingfactorAnalysismean[i][j]/replace)

                crossoverAveragevalue[j][0] = crossoverAveragevalue[j][0] + (crossoverAnalysismax[i][j]/replace)
                crossoverAveragevalue[j][1] = crossoverAveragevalue[j][1] + (crossoverAnalysismin[i][j]/replace)
                crossoverAveragevalue[j][2] = crossoverAveragevalue[j][2] + (crossoverAnalysismean[i][j]/replace)

                dimensionAverage[j][0] = dimensionAverage[j][0]+(dimensionAnalysismax[i][j]/replace)
                dimensionAverage[j][1] = dimensionAverage[j][1]+(dimensionAnalysismin[i][j]/replace)
                dimensionAverage[j][2] = dimensionAverage[j][2]+(dimensionAnalysismean[i][j]/replace)

                #print(acceptAnalysis[i][j])
                acceptAverage[j] = acceptAverage[j] + acceptAnalysis[i][j]/replace

        file_path = self.main_path+'/Scaling_Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'_scalingvalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Max','Min','Mean'])
            writer.writerows(scalingfactorAveragevalue)

        file_path = self.main_path+'/Scaling_Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'_crossovervalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Max','Min','Mean'])
            writer.writerows(crossoverAveragevalue)

        file_path = self.main_path+'/Scaling_Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'_dimensionvalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Max','Min','Mean'])
            writer.writerows(dimensionAverage)

        #print(acceptAverage)
        file_path = self.main_path+'/Scaling_Graph/'+self.functiontype+'/value/'+self.functionname+'_'+self.filename+'_acceptvalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Accept'])
            for i in range(replace):
                writer.writerow([acceptAverage[i]])

        scaling_show = scalingfactorAveragevalue
        crossover_show = crossoverAveragevalue
        dimensionshow = dimensionAverage
        print('Mutant vector strategy: ',self.strategy)
        print('Function: ',self.functionname,' with experiment ',self.filename)
        print('Minimized Solution average: ',np.average(minsolution))
        print('Minimized Solution Max: ',str(max(minsolution)),' Minimized Solution Min: ',str(min(minsolution)))
        print('Minimized Solution standart diviation: ',np.std(minsolution))
        print('Time find optimal solution: ',np.average(timecalculation)/60,' minuted Timeperround ',np.mean(time_perround[0]))
        print('Round find optimal solution: ',np.average(roundstable))
        print('Number of dimension change: Max ',np.max(dimensionshow[2]),' Min ',np.min(dimensionshow[2]),' Mean ',np.mean(dimensionshow[2]))
        print('Number of accept new soultion: Max ',np.max(acceptAverage),' Min ',np.min(acceptAverage),' Mean ',np.mean(acceptAverage))
        print('Crossover rate: Max ',np.max(crossover_show[2]),' Min ',np.min(crossover_show[2]),' Mean ',np.mean(crossover_show[2]))
        print('Scaling range: Max ',np.max(scaling_show[2]),' Min ',np.min(scaling_show[2]),' Mean ',np.mean(scaling_show[2]))
        print('=================================================================')

        #file_path = self.main_path+'/Graph/logfile/logfile_'+self.functionname+'_'+self.filename+'.txt'
        #file_path = 'C:/Users/patip/Documents/Python/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_'+str(crossover_rate)+'_description_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'.txt'
        #f = open(file_path,'a')
        #f.write('Minimized Solution average: '+str(np.average(minsolution))+'\n')
        #f.write('Minimized Solution Max: '+str(max(minsolution))+'Minimized Solution Min: '+str(min(minsolution))+'\n')
        #f.write('Minimized Solution standart diviation: '+str(np.std(minsolution))+'\n')
        #f.write('Time find optimal solution: '+str(np.average(timecalculation)/60)+' minuted Timeperround'+str(np.mean(time_perround[0]))+'\n')
        #f.write('Round find optimal solution: '+str(np.average(roundstable))+'\n')

        


        




    








