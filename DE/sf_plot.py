from DE_function_CPE_server_DSIDE_sf_value import DSIDE_Algorithm
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
import sys
sys.path.insert(0,main_path)
from Benchmark.functionbenchmark import Sphere as Sphere_fun
#from Benchmark.functionbenchmark import Elliptic as Elliptic_fun
#from Benchmark.functionbenchmark import Zakharov as Zakharov_fun

from Benchmark.functionbenchmark import HGBat as HGBat_fun
#from Benchmark.functionbenchmark import HappyCat as HappyCat_fun
from Benchmark.functionbenchmark import Scaffer2 as Scaffer2_fun
strategy1 = 'DE/rand/1'  
strategy2 = 'DE/best/1'
strategy3 = 'DE/rand/2'
strategy4 = 'DE/best/2'

strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(dimensiton=100,round=2000,functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-3sf_100di_line6'+strategy_name,cr=0.8)

DSIDE_obj = DSIDE_Algorithm(dimensiton=100,round=2000,functionname='HGBat',functioneveluate=HGBat_fun,strategy=strategy1,sf_fix=False,functiontype='MultimodalFunction')
DSIDE_obj.optimize(filename='DSIDE_1-3sf_100di_line6'+strategy_name,cr=0.8)

DSIDE_obj = DSIDE_Algorithm(dimensiton=100,round=2000,functionname='Scaffer2',functioneveluate=Scaffer2_fun,strategy=strategy1,sf_fix=False,functiontype='MultimodalFunction')
DSIDE_obj.optimize(filename='DSIDE_1-3sf_100di_line6'+strategy_name,cr=0.8)