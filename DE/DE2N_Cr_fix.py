import numpy as np
import csv
import random
from datetime import datetime
import sys
from tqdm.notebook import tqdm_notebook
from tqdm import tqdm
sys.path.insert(0,'/home/pythonrunnew/Algorithm')
#sys.path.insert(0,'C:/Users/patip/Documents/Python/Algorithm')
from Benchmark.functionbenchmark import Sphere as myfunc

#function_type = 'MultimodalFunction'
function_type = 'UnimodalFunction'
functionname = 'Sphere'
replace = 10
dimension = 30
populationsize = 500
lowerbound = -100
upperbound = 100
round = 2000
minimized_value = 0
maximized_value = 0
minuted = 0
minimized_value_round = np.zeros(round)
minimized_vector = np.zeros(dimension)
minimized_value_keep = np.zeros((round,3))
value_analysis = np.zeros((round,3))
time_perround = np.zeros((10,1))
value = np.zeros(populationsize)
population = np.zeros((populationsize,dimension))

#%% function
def build_trial_nearest(r_vector1:np.array,r_vector2:np.array,target:np.array,generation)->np.array:
    cr_rate = 0.8 #(0.8-(0.8-0.5))*(generation/round)       # 0.8 -> 0.5
    scale_factor = (0.2-(0.5-0.2))*(generation/round)  # 0.2 -> 0.5
    dummy_vector = np.random.uniform(low=0,high=1,size=dimension)
    weight = 0.8*cr_rate
    mutant_vector = weight*target+scale_factor*(r_vector1-target)+scale_factor*(r_vector2-target)
    trial = np.zeros(dimension)
    for i in range(dimension):
        if dummy_vector[i] > cr_rate:
            trial[i] = target[i]
        else:
            trial[i] = mutant_vector[i]

    return trial

def build_trial_best(best_vector:np.array,r_vector1:np.array,target:np.array,generation:float)-> np.array:
    cr_rate = 0.8  #(0.8-(0.8-0.5))*(generation/round) # 0.8 -> 0.5
    scale_factor = (0.2-(0.5-0.2))*(generation/round)  # 0.2 -> 0.5
    dummy_vector = np.random.uniform(low=0,high=1,size=dimension)
    weight = 0.8*(cr_rate)
    mutant_vector = weight*best_vector+scale_factor*(best_vector-target)+scale_factor*(r_vector1-target)
    trial = np.zeros(dimension)
    for i in range(dimension):
        if dummy_vector[i] > cr_rate:
            trial[i] = target[i]
        else:
            trial[i] = mutant_vector[i]
    return trial

def eveluate(fun,arg:np.array)->float:
    return fun(arg)

def distance_index(current_vector:np.array,all_vector:np.array)->int:
    distance_value = np.zeros(populationsize)
    for i in range(populationsize):
        distance_value[i] = np.linalg.norm(current_vector-all_vector[i])

    index_zeros = np.where(distance_value == 0)[0][0]
    dummy_distance = np.delete(distance_value,index_zeros,0)
    return np.where(distance_value == min(dummy_distance))[0][0]


def selection(trial_vector:np.array,target_vector:np.array,fun)->np.array:
    trial_value = eveluate(fun,trial_vector)
    target_value = eveluate(fun,target_vector)
    if trial_value <= target_value:
        return trial_vector
    else:
        return target_vector



#%% run program
lowerbound = -100
upperbound = 100

for k in range(replace):
    population = np.zeros((populationsize,dimension))
    for i in range(populationsize):
        dummy = np.random.uniform(low=lowerbound,high=upperbound+1,size=dimension)
        population[i:] = dummy

    now = datetime.now()
    for i in tqdm(range(round),desc="Function "+functionname+"_"+str(dimension)+"di_"+str(round)+"_"+str(populationsize)+"_run_"+str(k+1)):
        value = np.zeros(populationsize)
        population_dummy = np.zeros((populationsize,dimension))
        for j in range(populationsize):
            value[j] = eveluate(myfunc,population[j])

        if i == 0:
            minimized_value = min(value)
            index = np.where(value == minimized_value)[0][0]
            minimized_vector = population[index]
        
        for j in range(populationsize):
            if value[j] == 0:
                index = distance_index(population[j],population)
                vectorrand = np.random.permutation(populationsize)
                del_index = np.where(vectorrand==index)[0][0]
                vectorrand = np.delete(vectorrand,del_index,0)
                #del_index = np.where(vectorrand == j)[0][0]
                #vectorrand = np.delete(vectorrand,del_index,0)
                near_vector = population[index]
                rand_vector = population[vectorrand[0]]
                trial_vector = build_trial_nearest(r_vector1=near_vector,r_vector2=rand_vector,target=population[j],generation=(i+1))
            else:
                ratio = minimized_value/value[j]
                if ratio < 0.5:
                    vectorrand = np.random.permutation(populationsize)
                    del_index = np.where(vectorrand == j)[0][0]
                    vectorrand = np.delete(vectorrand,del_index,0)
                    rand_vector = population[vectorrand[0]]
                    trial_vector = build_trial_best(best_vector=minimized_vector,r_vector1=rand_vector,target=population[j],generation=(i+1))

                else:
                    index = distance_index(population[j],population)
                    vectorrand = np.random.permutation(populationsize)
                    del_index = np.where(vectorrand==index)[0][0]
                    vectorrand = np.delete(vectorrand,del_index,0)
                    #del_index = np.where(vectorrand == j)[0][0]
                    #vectorrand = np.delete(vectorrand,del_index,0)
                    near_vector = population[index]
                    rand_vector = population[vectorrand[0]]
                    trial_vector = build_trial_nearest(r_vector1=near_vector,r_vector2=rand_vector,target=population[j],generation=(i+1))

            population_dummy[j] = selection(trial_vector=trial_vector,target_vector=population[j],fun=myfunc)

        for j in range(populationsize):
            population[j] = population_dummy[j]
            value[j] = eveluate(myfunc,population[j])

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
    time_perround[k][0] = ((now3-now).seconds+((now3-now).microseconds)*1E-6)/round

    file_path = '/home/pythonrunnew/Algorithm/raw_reault/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_'+str(dimension)+'_run_'+str(k+1)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.csv'
    #file_path = 'C:/Users/patip/Documents/Python/Algorithm/raw_reault/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_'+str(dimension)+'_run_'+str(k+1)+'_population_'+str(populationsize)+'.csv'
    with open(file_path,'w',encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Solution','round','time'])
        writer.writerows(minimized_value_keep)


    file_path = '/home/pythonrunnew/Algorithm/analysis_result/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_analysis_'+str(dimension)+'_run_'+str(k+1)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.csv'
    #file_path = 'C:/Users/patip/Documents/Python/Algorithm/analysis_result/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_analysis_'+str(dimension)+'_run_'+str(k+1)+'_population_'+str(populationsize)+'.csv'
    with open(file_path,'w',encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['max','min','mean'])
        writer.writerows(value_analysis)

    #print('Round: ',(k+1),' finish')

file_path = '/home/pythonrunnew/Algorithm/time/DE2N_Cr_fix_'+functionname+'_timeperround_'+str(dimension)+'_population_'+str(populationsize)+'.csv'
#file_path = 'C:/Users/patip/Documents/Python/Algorithm/time/DE2N_Cr_fix_'+functionname+'_timeperround_'+str(dimension)+'_population_'+str(populationsize)+'.csv'
with open(file_path,'w',encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time_perround'])
        writer.writerows(time_perround)


#%% value use to graph
import pandas as pd
import csv
row_data = round
replace = 10

solution = np.zeros((replace,row_data))
solution_average = np.zeros((1,row_data))
minsolution = np.zeros(replace)
timecalculation = np.zeros(replace)
roundstable = np.zeros(replace)

for k in range(replace):
    path = '/home/pythonrunnew/Algorithm/raw_reault/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_'+str(dimension)+'_run_'+str(k+1)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.csv'
    #path = 'C:/Users/patip/Documents/Python/Algorithm/raw_reault/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_'+str(dimension)+'_run_'+str(k+1)+'_population_'+str(populationsize)+'.csv'
    my_sol = pd.read_csv(path,nrows=row_data)
    solution[k:] = my_sol['Solution']
    solution[k:] = my_sol['Solution']
    minsolution[k] = min(my_sol['Solution'])
    roundstable[k] = max(my_sol['round'])
    timecalculation[k] = max(my_sol['time'])

for j in range(row_data):
    for i in range(replace):
        solution_average[0][j] = solution_average[0][j] + (solution[i][j]/replace)

solution_average = np.transpose(solution_average)
# '/home/pythonrunnew/Algorithm/Graph/MultimodalFuntion/value/DE2N_Cr_fix_Scaffer2_30_population_100.csv'
file_path = '/home/pythonrunnew/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_fix_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.csv'
#file_path = 'C:/Users/patip/Documents/Python/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_fix_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'.csv'
with open(file_path,'w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Average'])
    writer.writerows(solution_average)

print(minsolution)

print('Minimized Solution average: ',np.average(minsolution))
print('Minimized Solution standart diviation: ',np.std(minsolution))
print('Time find optimal solution: ',np.average(timecalculation)/60,' minuted')
print('Round find optimal solution: ',np.average(roundstable))

#file_path = '/home/pythonrunnew/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_fix_description_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.txt'
file_path = 'C:/Users/patip/Documents/Python/Algorithm/Graph/'+function_type+'/value/DE2N_Cr_fix_description_'+functionname+'_'+str(dimension)+'_population_'+str(populationsize)+'.txt'
f = open(file_path,'a')
f.write('Minimized Solution Max: '+str(max(minsolution))+'\n')
f.write('Minimized Solution Min: '+str(min(minsolution))+'\n')
f.write('Minimized Solution average: '+str(np.average(minsolution))+'\n')
f.write('Minimized Solution standart diviation: '+str(np.std(minsolution))+'\n')
f.write('Time find optimal solution: '+str(np.average(timecalculation)/60)+' minuted'+'\n')
f.write('Round find optimal solution: '+str(np.average(roundstable))+'\n')



#%% analysis
row_data = round
replace = 10
result_analysis_max = np.zeros((replace,row_data))
result_analysis_min = np.zeros((replace,row_data))
result_analysis_mean = np.zeros((replace,row_data))

data_average = np.zeros((row_data,3))
for i in range(replace):
    path = '/home/pythonrunnew/Algorithm/analysis_result/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_analysis_'+str(dimension)+'_run_'+str(i+1)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.csv'
    #path = 'C:/Users/patip/Documents/Python/Algorithm/analysis_result/'+functionname+'_result/DE2N_Cr_fix_'+functionname+'_analysis_'+str(dimension)+'_run_'+str(i+1)+'_population_'+str(populationsize)+'.csv'
    print(path)
    my_sol = pd.read_csv(path,nrows=row_data)
    result_analysis_max[i:] = my_sol['max']
    result_analysis_min[i:] = my_sol['min']
    result_analysis_mean[i:] = my_sol['mean']

for j in range(row_data):
    for i in range(replace):
        data_average[j][0] =data_average[j][0] + (result_analysis_max[i][j]/10)
        data_average[j][1] =data_average[j][1] + (result_analysis_min[i][j]/10)
        data_average[j][2] =data_average[j][2] + (result_analysis_mean[i][j]/10)




file_path = '/home/pythonrunnew/Algorithm/Graph/'+function_type+'/analysis/DE2N_Cr_fix_'+functionname+'_analysis_'+str(dimension)+'_population_'+str(populationsize)+'_round_'+str(round)+'_.csv'
#file_path = 'C:/Users/patip/Documents/Python/Algorithm/Graph/'+function_type+'/analysis/DE2N_Cr_fix_'+functionname+'_analysis_'+str(dimension)+'_population_'+str(populationsize)+'.csv'
with open(file_path,'w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['max','min','mean'])
    writer.writerows(data_average)

