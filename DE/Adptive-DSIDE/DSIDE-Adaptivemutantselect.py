import sys
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
sys.path.insert(0,main_path)
from AdaptiveDSIDE2 import DSIDEselectionMutant
from AdaptiveDSIDE3 import  DSIDEwroseVector
from Benchmark.functionbenchmark import Sphere,Elliptic,Schwefel12,Schwefel221,Schwefel222,Zakharov
# from Benchmark.functionbenchmark import Bentcigar

Sphere_obj = DSIDEselectionMutant(functioneveluate=Sphere,functionname='Sphere',dimension=30,round=5000,populationsize=100)
Elliptic_obj = DSIDEselectionMutant(functioneveluate=Elliptic,functionname='Elliptic',dimension=30,round=5000,populationsize=100)
# Bentcigar_obj = DSIDEselectionMutant(functioneveluate=Bentcigar,functionname='Bentcigar',dimension=30,round=5000,populationsize=100)
Schwefel12_obj = DSIDEselectionMutant(functioneveluate=Schwefel12,functionname='Schwefel12',dimension=30,round=5000,populationsize=100)
Schwefel222_obj = DSIDEselectionMutant(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-10)
Schwefel221_obj = DSIDEselectionMutant(functioneveluate=Schwefel221,functionname='Schwefel221',dimension=30,round=5000,populationsize=100)
Zakharov_obj = DSIDEselectionMutant(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-5)

Sphere_obj.optimize(filename='DSIDEselectionMutant')
Elliptic_obj.optimize(filename='DSIDEselectionMutant')
# Bentcigar_obj.optimize(filename='DSIDEselectionMutant')
Schwefel12_obj.optimize(filename='DSIDEselectionMutant')
Schwefel222_obj.optimize(filename='DSIDEselectionMutant')
Schwefel221_obj.optimize(filename='DSIDEselectionMutant')
Zakharov_obj.optimize(filename='DSIDEselectionMutant')



Sphere_obj = DSIDEwroseVector(functioneveluate=Sphere,functionname='Sphere',dimension=30,round=5000,populationsize=100)
Elliptic_obj = DSIDEwroseVector(functioneveluate=Elliptic,functionname='Elliptic',dimension=30,round=5000,populationsize=100)
# Bentcigar_obj = DSIDEwroseVector(functioneveluate=Bentcigar,functionname='Bentcigar',dimension=30,round=5000,populationsize=100)
Schwefel12_obj = DSIDEwroseVector(functioneveluate=Schwefel12,functionname='Schwefel12',dimension=30,round=5000,populationsize=100)
Schwefel222_obj = DSIDEwroseVector(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-10)
Schwefel221_obj = DSIDEwroseVector(functioneveluate=Schwefel221,functionname='Schwefel221',dimension=30,round=5000,populationsize=100)
Zakharov_obj = DSIDEwroseVector(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-5)

Sphere_obj.optimize(filename='DSIDEwroseVector')
Elliptic_obj.optimize(filename='DSIDEwroseVector')
# Bentcigar_obj.optimize(filename='DSIDEwroseVector')
Schwefel12_obj.optimize(filename='DSIDEwroseVector')
Schwefel222_obj.optimize(filename='DSIDEwroseVector')
Schwefel221_obj.optimize(filename='DSIDEwroseVector')
Zakharov_obj.optimize(filename='DSIDEwroseVector')

