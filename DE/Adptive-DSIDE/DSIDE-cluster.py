import sys
#main_path= 'C:/Users/patip/Documents/Python/StandartAlgorithm'
#main_path = '/home/pythonrunnew/StandartAlgorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'

sys.path.insert(0,main_path)
from AdptiveDSIDE import DSIDEclustering
from Benchmark.functionbenchmark import Sphere

Sphere_obj = DSIDEclustering(functioneveluate=Sphere,functionname='Sphere',lowerbound=-100,upperbound=100,round=30)
Sphere_obj.optimize(filename='DSIDE-Kmean')