import sys
# main_path= 'C:/Users/patip/OneDrive/Documents/python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
sys.path.insert(0,main_path)
from AdaptiveDSIDE7 import DSIDEmixVector
from Benchmark.functionbenchmark import HGBat,Scaffer_F6,Scaffer2,HappyCat
# from Benchmark.functionbenchmark import Scaffer2,Scaffer_F6,HappyCat,HGBat
# from Benchmark.functionbenchmark import Bentcigar

HGBat_obj = DSIDEmixVector(functioneveluate=HGBat,functionname='HGBat',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
Scaffer_F6_obj = DSIDEmixVector(functioneveluate=Scaffer_F6,functionname='Scaffer_F6',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
Scaffer2_obj = DSIDEmixVector(functioneveluate=Scaffer2,functionname='Scaffer2',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
# Schwefel222_obj = DSIDEmixVector(functioneveluate=Schwefel222,functionname='Schwefel222',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction',upperbound=10,lowerbound=-10)
HappyCat_obj = DSIDEmixVector(functioneveluate=HappyCat,functionname='HappyCat',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction')
# Zakharov_obj = DSIDEmixVector(functioneveluate=Zakharov,functionname='Zakharov',dimension=30,round=5000,populationsize=100,functiontype='MultimodalFunction',upperbound=10,lowerbound=-5)

HGBat_obj.optimize(filename='DSIDEmixVectorpopulation')
Scaffer_F6_obj.optimize(filename='DSIDEmixVectorpopulation')
Scaffer2_obj.optimize(filename='DSIDEmixVectorpopulation')
# Schwefel222_obj.optimize(filename='DSIDEmixVectorpopulation')
HappyCat_obj.optimize(filename='DSIDEmixVectorpopulation')
# Zakharov_obj.optimize(filename='DSIDEmixVectorpopulation')

