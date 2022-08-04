import sys
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
sys.path.insert(0,main_path)
from AnanelingDSIDE import DSIDEanaelingSelection
from Benchmark.functionbenchmark import Sphere,Elliptic,Schwefel12,Schwefel221,Schwefel222,Zakharov
# from Benchmark.functionbenchmark import Bentcigar

Sphere_obj = DSIDEanaelingSelection(functioneveluate=Sphere,functionname='Sphere',dimension=30,round=5000,populationsize=100)
Elliptic_obj = DSIDEanaelingSelection(functioneveluate=Elliptic,functionname='Elliptic',dimension=30,round=5000,populationsize=100)
# Bentcigar_obj = DSIDEanaelingSelection(functioneveluate=Bentcigar,functionname='Bentcigar',dimension=30,round=5000,populationsize=100)
Schwefel12_obj = DSIDEanaelingSelection(functioneveluate=Schwefel12,functionname='Schwefel12',dimension=30,round=5000,populationsize=100)
Schwefel222_obj = DSIDEanaelingSelection(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-10)
Schwefel221_obj = DSIDEanaelingSelection(functioneveluate=Schwefel221,functionname='Schwefel221',dimension=30,round=5000,populationsize=100)
Zakharov_obj = DSIDEanaelingSelection(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=100,upperbound=10,lowerbound=-5)

Sphere_obj.optimize(filename='DSIDEanaelingSelection')
Elliptic_obj.optimize(filename='DSIDEanaelingSelection')
# Bentcigar_obj.optimize(filename='DSIDEanaelingSelection')
Schwefel12_obj.optimize(filename='DSIDEanaelingSelection')
Schwefel222_obj.optimize(filename='DSIDEanaelingSelection')
Schwefel221_obj.optimize(filename='DSIDEanaelingSelection')
Zakharov_obj.optimize(filename='DSIDEanaelingSelection')