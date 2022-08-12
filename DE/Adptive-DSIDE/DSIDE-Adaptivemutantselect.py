import sys
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
sys.path.insert(0,main_path)
from AdaptiveDSIDE4 import DSIDEmedianVector
from Benchmark.functionbenchmark import Sphere,Elliptic,Schwefel12,Schwefel221,Schwefel222,Zakharov
# from Benchmark.functionbenchmark import Bentcigar

Sphere_obj = DSIDEmedianVector(functioneveluate=Sphere,functionname='Sphere',dimension=30,round=5000,populationsize=500)
Elliptic_obj = DSIDEmedianVector(functioneveluate=Elliptic,functionname='Elliptic',dimension=30,round=5000,populationsize=500)
Schwefel12_obj = DSIDEmedianVector(functioneveluate=Schwefel12,functionname='Schwefel12',dimension=30,round=5000,populationsize=500)
Schwefel222_obj = DSIDEmedianVector(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=500,upperbound=10,lowerbound=-10)
Schwefel221_obj = DSIDEmedianVector(functioneveluate=Schwefel221,functionname='Schwefel221',dimension=30,round=5000,populationsize=500)
Zakharov_obj = DSIDEmedianVector(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=500,upperbound=10,lowerbound=-5)

Sphere_obj.optimize(filename='DSIDEmedianVector500population')
Elliptic_obj.optimize(filename='DSIDEmedianVector500population')
Schwefel12_obj.optimize(filename='DSIDEmedianVector500population')
Schwefel222_obj.optimize(filename='DSIDEmedianVector500population')
Schwefel221_obj.optimize(filename='DSIDEmedianVector500population')
Zakharov_obj.optimize(filename='DSIDEmedianVector500population')

