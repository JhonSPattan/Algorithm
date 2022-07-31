from DE_function_CPE_server import DSIDE_Algorithm
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
strategy3 = 'DE/rand/2'
strategy4 = 'DE/best/2'


#%% Sphere function
#%%DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)

#%%DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy2,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy2,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)



#%%DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy3,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy3,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%DE/rand/2
strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy4,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy4,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)




#%% Elliptic function
#%%DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)

#%%DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy2,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy2,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)



#%%DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy3,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy3,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%DE/rand/2
strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy4,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy4,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%% Zakharov function
#%%DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)

#%%DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy2,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy2,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)



#%%DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy3,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy3,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%DE/rand/2
strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy4,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy4,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%HGBat function
#%%DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)

#%%DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy2,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy2,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)



#%%DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy3,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy3,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%DE/rand/2
strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy4,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy4,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%HappyCat function
#%%DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)

#%%DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy2,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy2,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)



#%%DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy3,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy3,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%DE/rand/2
strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy4,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy4,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)





#%%Scaffer2 function
#%%DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)

#%%DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy2,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy2,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)



#%%DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy3,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy3,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)


#%%DE/rand/2
strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_1-1line1'+strategy_name,cr=0.4,sf=0.2)
DSIDE_obj.optimize(filename='DSIDE_1-1line2'+strategy_name,cr=0.4,sf=0.3)
DSIDE_obj.optimize(filename='DSIDE_1-1line3'+strategy_name,cr=0.4,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy4,sf_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_1-1line4'+strategy_name,cr=0.4,sf_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_1-1line5'+strategy_name,cr=0.4)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy4,sf_fix=False)
DSIDE_obj.optimize(filename='DSIDE_1-1line6'+strategy_name,cr=0.4)





