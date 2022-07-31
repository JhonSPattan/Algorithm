from DE.sf_plot import DSIDE_obj
from DE_function_CPE_server_DSIDE_forexp3 import DSIDE_Algorithm
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
import sys
sys.path.insert(0,main_path)
from Benchmark.functionbenchmark import Sphere as Sphere_fun
from Benchmark.functionbenchmark import Elliptic as Elliptic_fun
from Benchmark.functionbenchmark import Zakharov as Zakharov_fun

from Benchmark.functionbenchmark import HGBat as HGBat_fun
from Benchmark.functionbenchmark import HappyCat as HappyCat_fun
from Benchmark.functionbenchmark import Scaffer2 as Scaffer2_fun
strategy1 = 'DE/rand/1'  
strategy2 = 'DE/best/1'

strategyname = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functioneveluate=Sphere_fun,functionname='Sphere',round=5,strategy=strategy1)
DSIDE_obj.optimize(filename='NewExp_line1'+strategyname)

DSIDE_obj = DSIDE_Algorithm(functioneveluate=Sphere_fun,functionname='Sphere',round=5,strategy=strategy1,equlationoption='random_compare')
DSIDE_obj.optimize(filename='NewExp_line2'+strategyname)
