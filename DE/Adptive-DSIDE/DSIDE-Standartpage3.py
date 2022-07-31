import sys
#main_path= 'C:/Users/patip/Documents/Python/StandartAlgorithm'
#main_path = '/home/pythonrunnew/StandartAlgorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'
sys.path.insert(0,main_path)
from AdptiveDSIDE import DSIDEselectMutant
from Benchmark.functionbenchmark import Penalized,Whitley,Salomon

Penalized_Obj = DSIDEselectMutant(functioneveluate=Penalized,functionname='Penalized',functiontype='MultimodalFunction',lowerbound=-50,upperbound=50,round=2000)
Whitley_Obj = DSIDEselectMutant(functioneveluate=Whitley,functionname='Whitley',functiontype='MultimodalFunction',lowerbound=-10.24,upperbound=10.24,round=2000)

Penalized_Obj.optimize(filename='AdptiveDSIDE')
Whitley_Obj.optimize(filename='AdptiveDSIDE')