import sys
#main_path= 'C:/Users/patip/Documents/Python/StandartAlgorithm'
#main_path = '/home/pythonrunnew/StandartAlgorithm'
main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'
sys.path.insert(0,main_path)
from AdptiveDSIDE import DSIDEselectMutant
from Benchmark.functionbenchmark import Rosenbrock
from Benchmark.functionbenchmark import Salomon
from Benchmark.functionbenchmark import Scaffer_F6

Rosenbrock_Obj = DSIDEselectMutant(functioneveluate=Rosenbrock,functionname='Rosenbrock',functiontype='MultimodalFunction',lowerbound=-30,upperbound=30,round=2000)
Salomon_Obj = DSIDEselectMutant(functioneveluate=Salomon,functionname='Salomon',functiontype='MultimodalFunction',lowerbound=-100,upperbound=100,round=2000)
ScafferF6_Obj = DSIDEselectMutant(functioneveluate=Scaffer_F6,functionname='Scaffer_F6',functiontype='MultimodalFunction',lowerbound=-100,upperbound=100,round=2000)

Rosenbrock_Obj.optimize(filename='AdptiveDSIDE')
Salomon_Obj.optimize(filename='AdptiveDSIDE')
ScafferF6_Obj.optimize(filename='AdptiveDSIDE')


