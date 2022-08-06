from pyclbr import Function
import numpy as np
import pandas as pd
import collections
import csv
import random
import os
import math
from datetime import  datetime


#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'


class DSIDEwroseVector():
    def __init__(self,functioneveluate:Function,functionname:str,functiontype:str='UnimodalFunction',dimension:int=30,lowerbound:float=-100,upperbound:float=100,round:float=2000,populationsize:int=100,problemtype:str='Small'):
        self.functioneveluate = functioneveluate
        self.functionname = functionname
        self.functiontype = functiontype
        self.dimension = dimension
        self.lowerbound = lowerbound
        self.upperbound = upperbound
        self.round = round
        self.populationsize = populationsize
        self.main_path = main_path
        self.randomvalue = random.uniform(0,1)
        self.problemtype = problemtype
        self.crossoverRate = 0
        self.scalingFactor = 0
        self.alpha = 0
    
    def selectionWroseMutant(self,component:np.array)->tuple:
        mutantList = []
        fitnessList = []
        mutantList.append(self.alpha*component[0]+self.scalingFactor*(component[1]-component[2]))
        mutantList.append(self.alpha*component[0]+self.scalingFactor*(component[2]-component[1]))
        mutantList.append(self.alpha*component[1]+self.scalingFactor*(component[0]-component[2]))
        mutantList.append(self.alpha*component[1]+self.scalingFactor*(component[2]-component[0]))
        mutantList.append(self.alpha*component[2]+self.scalingFactor*(component[0]-component[1]))
        mutantList.append(self.alpha*component[2]+self.scalingFactor*(component[1]-component[0]))

        mutantList = np.array(mutantList)
        for i in range(6):
            fitnessList.append(self.functioneveluate(mutantList[i]))
        fitnessList = np.array(fitnessList)
        indexMax = np.where(max(fitnessList)==fitnessList)[0][0]
        return mutantList[indexMax],(indexMax+1)

    def buildTrialVector(self,rVector1:np.array,rVector2:np.array,rVector3:np.array,targetVector:np.array)->tuple:
        component = np.array([rVector1,rVector2,rVector3])
        dummyVector = np.random.uniform(low=0,high=1,size=self.dimension)
        trial = np.zeros(self.dimension)
        dTrial = np.zeros(self.dimension)
        crossoverCount = 0
        dimensionCount = 0
        mutantSelect = 0
        mutantVector,mutantSelect = self.selectionWroseMutant(component=component)
        for i in range(self.dimension):
            if dummyVector[i] > self.crossoverRate:
                dTrial[i] = targetVector[i]
            else:
                dTrial[i] = mutantVector[i]
                crossoverCount = crossoverCount+1
        
        for i in range(self.dimension):
            if dTrial[i] > self.upperbound:
                dTrial[i] = self.upperbound
            elif dTrial[i] < self.lowerbound:
                dTrial[i] = self.lowerbound

        trial = dTrial
        dimensionCount = crossoverCount
        
        return trial,dimensionCount,mutantSelect
    
    def selection(self,trialVector:np.array,targetVector:np.array)->np.array:
        trialValue = self.functioneveluate(trialVector)
        targetValue = self.functioneveluate(targetVector)
        if trialValue <= targetValue:
            return trialVector
        else:
            return targetVector
    
    def optimize(self,filename:str):
        self.filename = filename
        self.crossovercount = np.zeros((self.round,3))
        replace = 5
        minimizedValue = 0
        maximizedValue = 0
        minuted = 0
        minimizedValueRound = np.zeros(self.round)
        minimizedValueKeep = np.zeros((self.round,3))
        # valueAnalysis = np.zeros((self.round,3))
        timePerround = np.zeros((replace,1))

        crossoverrateValuedata = np.zeros((self.round,3))
        crossoverrateInpopulation = np.zeros(self.populationsize)

        scalingfactorValuedata = np.zeros((self.round,3))
        scalingfactorInpopulation = np.zeros(self.populationsize)

        dimensionChangecount = np.zeros((self.round,3))
        dimensionChangeInpopulation = np.zeros(self.populationsize)

        selectMutant = []
        for k in range(replace):
            population = np.random.uniform(low=self.lowerbound,high=self.upperbound,size=(self.populationsize,self.dimension))
            acceptCountinpopulation = np.zeros((self.round,1))
            value = np.zeros(self.populationsize)
            now = datetime.now()
            for i in range(self.round):
                generationValue = pow(1-(i+1)/self.round,2)
                self.alpha =  1-pow(self.randomvalue,generationValue)
                for j in range(self.populationsize):
                    value[j] = self.functioneveluate(population[j])
                
                now2 = datetime.now()
                if i == 0 or minimizedValue > min(value):
                    minimizedValue = min(value)
                    maximizedValue = max(value)
                    minimizedValueRound[i] = minimizedValue
                    minRound = (i+1)
                    minuted = (now2-now).seconds
                
                minimizedValueKeep[i][0] = minimizedValue
                minimizedValueKeep[i][1] = minRound
                minimizedValueKeep[i][2] = minuted

                # valueAnalysis[i][0] = maximizedValue
                # valueAnalysis[i][1] = minimizedValue
                # valueAnalysis[i][2] = np.mean(value)

                populationDummy = np.zeros((self.populationsize,self.dimension))
                for j in range(self.populationsize):
                    if np.mean(value) == 0:
                        crossoverrateInpopulation[j] = 0
                        scalingfactorInpopulation[j] = 0
                        dimensionChangeInpopulation[j] = 0
                        continue
                    self.scalingFactor = (max(value)-value[j])/np.mean(value)
                    self.crossoverRate = (value[j]-min(value))/np.mean(value)
                    crossoverrateInpopulation[j] = self.crossoverRate
                    scalingfactorInpopulation[j] = self.scalingFactor
                    vectorRand = np.random.permutation(self.populationsize)
                    delIndex = np.where(vectorRand == j)[0][0]
                    vectorRand = np.delete(vectorRand,delIndex,0)
                    trialVector,dimensionChangeInpopulation[j],selectDummy = self.buildTrialVector(rVector1=population[vectorRand[0]],rVector2=population[vectorRand[1]],rVector3=population[vectorRand[2]],targetVector=population[j])
                    selectMutant.append(selectDummy)
                    populationDummy[j] = self.selection(trialVector=trialVector,targetVector=population[j])
                    if(populationDummy[j] == trialVector).all():
                        acceptCountinpopulation[i][0] = acceptCountinpopulation[i][0]+1
                
                crossoverrateValuedata[i][0] = np.max(crossoverrateInpopulation)
                crossoverrateValuedata[i][1] = np.min(crossoverrateInpopulation)
                crossoverrateValuedata[i][2] = np.mean(crossoverrateInpopulation)

                scalingfactorValuedata[i][0] = np.max(scalingfactorInpopulation)
                scalingfactorValuedata[i][1] = np.min(scalingfactorInpopulation)
                scalingfactorValuedata[i][2] = np.mean(scalingfactorInpopulation)

                dimensionChangecount[i][0] = np.max(dimensionChangeInpopulation)
                dimensionChangecount[i][1] = np.min(dimensionChangeInpopulation)
                dimensionChangecount[i][2] = np.mean(dimensionChangeInpopulation)

                population = populationDummy


            now3 = datetime.now()
            timePerround[k][0] = ((now3-now).seconds+((now3-now).microseconds)*1E-6)/self.round

            mutantVal = collections.Counter(np.array(selectMutant))
            barchart = np.zeros((6,2))
            for i in range(1,7):
                barchart[i-1][0] = i
                barchart[i-1][1] = mutantVal[i]
                
            file_path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_indexselect_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Index','Count'])
                writer.writerows(barchart)

            file_path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_'+self.filename+'_run_'+str(k+1)+'.csv'
            with open(file_path,'w',encoding='UTF8',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Solution','round','time'])
                writer.writerows(minimizedValueKeep)

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
                    writer.writerow([acceptCountinpopulation[jk][0]])

        file_path = self.main_path+'/time/'+self.filename+'_timeperround.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['time_perround'])
            writer.writerows(timePerround)

        solution = np.zeros((replace,self.round))
        solution_average = np.zeros((1,self.round))
        minsolution = np.zeros(replace)
        timecalculation = np.zeros(replace)
        roundstable = np.zeros(replace)

        barchart = np.zeros((6,2))
        barchart[0][0] = 1
        barchart[1][0] = 2
        barchart[2][0] = 3
        barchart[3][0] = 4
        barchart[4][0] = 5
        barchart[5][0] = 6
        for k in range(replace):
            path = self.main_path+'/raw_result/'+self.functionname+'_result/'+self.functionname+'_indexselect_'+self.filename+'_run_'+str(k+1)+'.csv'
            my_sol = pd.read_csv(path,nrows=6)
            for i in range(6):
                barchart[i][1] = barchart[i][1]+my_sol['Count'][i]/5
            os.remove(path=path)

        file_path = self.main_path+'/Indexselect/'+self.functiontype+'/value-'+self.problemtype+'/'+self.functionname+'_indexselect_'+self.filename+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Index','Count'])
            writer.writerows(barchart)

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
        file_path = self.main_path+'/Graph/'+self.functiontype+'/value-'+self.problemtype+'/'+self.functionname+'_'+self.filename+'.csv'
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

        #print(acceptAverage)
        file_path = self.main_path+'/Scaling/'+self.functiontype+'/value-'+self.problemtype+'/'+self.functionname+'_'+self.filename+'_scalingvalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Max','Min','Mean'])
            writer.writerows(scalingfactorAveragevalue)

        file_path = self.main_path+'/Crossover/'+self.functiontype+'/value-'+self.problemtype+'/'+self.functionname+'_'+self.filename+'_crossovervalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Max','Min','Mean'])
            writer.writerows(crossoverAveragevalue)

        file_path = self.main_path+'/Dimension/'+self.functiontype+'/value-'+self.problemtype+'/'+self.functionname+'_'+self.filename+'_dimensionvalue'+'.csv'
        with open(file_path,'w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Max','Min','Mean'])
            writer.writerows(dimensionAverage)


        scaling_show = scalingfactorAveragevalue
        crossover_show = crossoverAveragevalue
        dimensionshow = dimensionAverage


        print('Adaptive DSIDE mutant select result of :',self.functiontype,'\t function name: ',self.functionname,flush=True)
        print('Function: ',self.functionname,' with experiment ',self.filename,flush=True)
        print('Minimized Solution average: ',np.average(minsolution),flush=True)
        print('Minimized Solution Max: ',str(max(minsolution)),' Minimized Solution Min: ',str(min(minsolution)),flush=True)
        print('Minimized Solution standart diviation: ',np.std(minsolution),flush=True)
        print('Time find optimal solution: ',np.average(roundstable)*np.average(timePerround),' minuted Timeperround ',np.average(timePerround),flush=True)
        print('Round find optimal solution: ',np.average(roundstable),flush=True)
        print('Number of dimension change: Max ',np.max(dimensionshow[2]),' Min ',np.min(dimensionshow[2]),' Mean ',np.mean(dimensionshow[2]),flush=True)
        print('Number of accept new soultion: Max ',np.max(acceptAverage),' Min ',np.min(acceptAverage),' Mean ',np.mean(acceptAverage),flush=True)
        print('Crossover rate: Max ',np.max(crossover_show[2]),' Min ',np.min(crossover_show[2]),' Mean ',np.mean(crossover_show[2]),flush=True)
        print('Scaling range: Max ',np.max(scaling_show[2]),' Min ',np.min(scaling_show[2]),' Mean ',np.mean(scaling_show[2]),flush=True)
        print('=================================================================',flush=True)