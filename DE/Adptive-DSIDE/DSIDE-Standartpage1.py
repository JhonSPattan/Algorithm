import sys
#main_path= 'C:/Users/patip/Documents/Python/StandartAlgorithm'
#main_path = '/home/pythonrunnew/StandartAlgorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'
sys.path.insert(0,main_path)
from AdptiveDSIDE import DSIDEselectMutant
from Benchmark.functionbenchmark import HGBat
from Benchmark.functionbenchmark import HappyCat
from Benchmark.functionbenchmark import Scaffer2

HGBat_Obj = DSIDEselectMutant(functioneveluate=HGBat,functionname='HGBat',functiontype='MultimodalFunction',lowerbound=-100,upperbound=100,round=2000)
HappyCat_Obj = DSIDEselectMutant(functioneveluate=HappyCat,functionname='HappyCat',functiontype='MultimodalFunction',lowerbound=-100,upperbound=100,round=2000)
Scaffer2_Obj = DSIDEselectMutant(functioneveluate=Scaffer2,functionname='Scaffer2',functiontype='MultimodalFunction',lowerbound=-100,upperbound=100,round=2000)

HGBat_Obj.optimize(filename='AdptiveDSIDE')
HappyCat_Obj.optimize(filename='AdptiveDSIDE')
Scaffer2_Obj.optimize(filename='AdptiveDSIDE')