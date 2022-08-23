import sys
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'
sys.path.insert(0,main_path)
from DSIDE import StandartDSIDE
from Benchmark.functionbenchmark import HGBat,Scaffer_F6,Scaffer2,HappyCat


# from Benchmark.functionbenchmark import Bentcigar

HGBat_obj = StandartDSIDE(functioneveluate=HGBat,functionname='HGBat',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
Scaffer_F6_obj = StandartDSIDE(functioneveluate=Scaffer_F6,functionname='Scaffer_F6',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
# Bentcigar_obj = StandartDSIDE(functioneveluate=Bentcigar,functionname='Bentcigar',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
Scaffer2_obj = StandartDSIDE(functioneveluate=Scaffer2,functionname='Scaffer2',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
# Schwefel222_obj = StandartDSIDE(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction',upperbound=10,lowerbound=-10)
HappyCat_obj = StandartDSIDE(functioneveluate=HappyCat,functionname='HappyCat',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
# Zakharov_obj = StandartDSIDE(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction',upperbound=10,lowerbound=-5)

HGBat_obj.optimize(filename='StandartDSIDE')
Scaffer_F6_obj.optimize(filename='StandartDSIDE')
# Bentcigar_obj.optimize(filename='StandartDSIDE')
Scaffer2_obj.optimize(filename='StandartDSIDE')
# Schwefel222_obj.optimize(filename='StandartDSIDE')
HappyCat_obj.optimize(filename='StandartDSIDE')
# Zakharov_obj.optimize(filename='StandartDSIDE')