from DE_function_CPE_server import DSIDE_Algorithm
#from tqdm import tqdm
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
#main_path = '/home/pythonrunnew/Algorithm'
main_path = '/myweb/www/pythonrunnew/Algorithm'
strategy1 = 'DE/rand/1'
import sys
sys.path.insert(0,main_path)
from Benchmark.functionbenchmark import Sphere as Sphere_fun
from Benchmark.functionbenchmark import Elliptic as Elliptic_fun
from Benchmark.functionbenchmark import Zakharov as Zakharov_fun

from Benchmark.functionbenchmark import HGBat as HGBat_fun
from Benchmark.functionbenchmark import HappyCat as HappyCat_fun
from Benchmark.functionbenchmark import Scaffer2 as Scaffer2_fun

#%% 30dimension
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,dimensiton=30,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_30dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,dimensiton=30,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_30dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,dimensiton=30,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_30dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=30,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_30dimension')


DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=30,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_30dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=30,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_30dimension')



#%% 100dimension
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,dimensiton=100,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_100dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,dimensiton=100,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_100dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,dimensiton=100,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_100dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=100,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_100dimension')


DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=100,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_100dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=100,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_100dimension')





#%% 500dimension
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,dimensiton=500,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_500dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,dimensiton=500,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_500dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,dimensiton=500,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_500dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=500,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_500dimension')


DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=500,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_500dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=500,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_500dimension')



#%% 1000dimension
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,dimensiton=1000,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1000dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,dimensiton=1000,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1000dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,dimensiton=1000,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1000dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=1000,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1000dimension')


DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=1000,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1000dimension')

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,dimensiton=1000,cr_fix=False,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1000dimension')
