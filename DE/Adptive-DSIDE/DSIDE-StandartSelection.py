import sys
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'
sys.path.insert(0,main_path)
from DSIDE import StandartDSIDE
from Benchmark.functionbenchmark import Sphere,Elliptic,Schwefel12,Schwefel221,Schwefel222,Zakharov
# from Benchmark.functionbenchmark import Bentcigar

Sphere_obj = StandartDSIDE(functioneveluate=Sphere,functionname='Sphere',dimension=30,round=5000,populationsize=100)
Elliptic_obj = StandartDSIDE(functioneveluate=Elliptic,functionname='Elliptic',dimension=30,round=5000,populationsize=100)
# Bentcigar_obj = StandartDSIDE(functioneveluate=Bentcigar,functionname='Bentcigar',dimension=30,round=5000,populationsize=100)
Schwefel12_obj = StandartDSIDE(functioneveluate=Schwefel12,functionname='Schwefel12',dimension=30,round=5000,populationsize=100)
Schwefel222_obj = StandartDSIDE(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-10)
Schwefel221_obj = StandartDSIDE(functioneveluate=Schwefel221,functionname='Schwefel221',dimension=30,round=5000,populationsize=100)
Zakharov_obj = StandartDSIDE(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-5)

Sphere_obj.optimize(filename='StandartDSIDE')
Elliptic_obj.optimize(filename='StandartDSIDE')
# Bentcigar_obj.optimize(filename='StandartDSIDE')
Schwefel12_obj.optimize(filename='StandartDSIDE')
Schwefel222_obj.optimize(filename='StandartDSIDE')
Schwefel221_obj.optimize(filename='StandartDSIDE')
Zakharov_obj.optimize(filename='StandartDSIDE')