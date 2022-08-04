import sys
#main_path= 'C:/Users/patip/Documents/Python/StandartAlgorithm'
#main_path = '/home/pythonrunnew/StandartAlgorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'

sys.path.insert(0,main_path)
from AdptiveDSIDE import DSIDEclustering
from Benchmark.functionbenchmark import Sphere
from Benchmark.functionbenchmark import HGBat



#Sphere_obj = DSIDEclustering(functioneveluate=Sphere,functionname='Sphere',lowerbound=-100,upperbound=100,round=2000)
#Sphere_obj.optimize(filename='DSIDE-Kmean')

HGBat_obj = DSIDEclustering(functioneveluate=HGBat,functionname='HGBat',functiontype='MultimodalFunction',lowerbound=-100,upperbound=100,round=2000)
HGBat_obj.optimize(filename='DSIDE-Kmean')
