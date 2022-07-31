from DE_function import DE2N_Algorithm
from DE_function import DSIDE_Algorithm
#main_path= 'C:/Users/patip/Documents/Python/Algorithm'
main_path = '/home/pythonrunnew/Algorithm'
#main_path = '/myweb/www/pythonrunnew/Algorithm'
import sys
sys.path.insert(0,main_path)
from Benchmark.functionbenchmark import Sphere as Sphere_fun
from Benchmark.functionbenchmark import Elliptic as Elliptic_fun
from Benchmark.functionbenchmark import Zakharov as Zakharov_fun

from Benchmark.functionbenchmark import HGBat as HGBat_fun
from Benchmark.functionbenchmark import HappyCat as HappyCat_fun
from Benchmark.functionbenchmark import Scaffer2 as Scaffer2_fun

#%% Experiment 3-1 Sphere function
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-1line1',functioneveluate=Sphere_fun,functionname='Sphere',cr_fix=False,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,cr_lower=0.5,sf_lower=0.2,sf_upper=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-1line2',functioneveluate=Sphere_fun,functionname='Sphere',cr_fix=False,sf_fix=False)
DSIDE_obj.optimize()

#%% Experiment 3-1 Elliptic function
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-1line1',functioneveluate=Elliptic_fun,functionname='Elliptic',cr_fix=False,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,cr_lower=0.5,sf_lower=0.2,sf_upper=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-1line2',functioneveluate=Elliptic_fun,functionname='Elliptic',cr_fix=False,sf_fix=False)
DSIDE_obj.optimize()

#%% Experiment 3-1 Zakharov function
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-1line1',functioneveluate=Zakharov_fun,functionname='Zakharov',cr_fix=False,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,cr_lower=0.5,sf_lower=0.2,sf_upper=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-1line2',functioneveluate=Zakharov_fun,functionname='Zakharov',cr_fix=False,sf_fix=False)
DSIDE_obj.optimize()

#%% Experiment 3-1 HGBat function
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-1line1',functioneveluate=HGBat_fun,functionname='HGBat',cr_fix=False,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,cr_lower=0.5,sf_lower=0.2,sf_upper=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-1line2',functioneveluate=HGBat_fun,functionname='HGBat',cr_fix=False,sf_fix=False)
DSIDE_obj.optimize()

#%% Experiment 3-1 HappyCat function
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-1line1',functioneveluate=HappyCat_fun,functionname='HappyCat',cr_fix=False,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,cr_lower=0.5,sf_lower=0.2,sf_upper=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-1line2',functioneveluate=HappyCat_fun,functionname='HappyCat',cr_fix=False,sf_fix=False)
DSIDE_obj.optimize()

#%% Experiment 3-1 Scaffer2 function
DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-1line1',functioneveluate=Scaffer2_fun,functionname='Scaffer2',cr_fix=False,sf_fix=False)
DE2N_obj.optimize(cr_upper=0.8,cr_lower=0.5,sf_lower=0.2,sf_upper=0.5)

DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-1line2',functioneveluate=Scaffer2_fun,functionname='Scaffer2',cr_fix=False,sf_fix=False)
DSIDE_obj.optimize()


#%% Experiment 3-2 Sphere function
""" DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-2line1',functioneveluate=Sphere_fun,functionname='Sphere')
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)

DE2N_obj = DE2N_Algorithm(filename='DE2N_Exp3-2line2',functioneveluate=Sphere_fun,functionname='Sphere')
DE2N_obj.optimize(cr_upper=0.8,sf_lower=0.2)


DSIDE_obj = DSIDE_Algorithm(filename='DE2N_Exp3-2line3',functioneveluate=Sphere_fun,functionname='Sphere')
DSIDE_obj.optimize() """


