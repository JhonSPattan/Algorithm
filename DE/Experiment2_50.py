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
#%%Sphere Function
#DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy1,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy2,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy2,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy3,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy3,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy4,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Sphere',functioneveluate=Sphere_fun,strategy=strategy4,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#%%Elliptic Function
#DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy1,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy2,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy2,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy3,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy3,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy4,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Elliptic',functioneveluate=Elliptic_fun,strategy=strategy4,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#%%Zakharov Function
#DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy1,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy2,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy2,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy3,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy3,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy4,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Zakharov',functioneveluate=Zakharov_fun,strategy=strategy4,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



#%%HGBat Function
#DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy1,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy2,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy2,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy3,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy3,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy4,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HGBat',functioneveluate=HGBat_fun,functiontype='MultimodalFunction',strategy=strategy4,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#%%HappyCat Function
#DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy1,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy2,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy2,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy3,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy3,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy4,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='HappyCat',functioneveluate=HappyCat_fun,functiontype='MultimodalFunction',strategy=strategy4,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)




#%%Scaffer2 Function
#DE/rand/1
strategy_name = '-DE_rand_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy1,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)

#DE/best/1
strategy_name = '-DE_best_1'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy2)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy2,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy2,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)


#DE/rand/2
strategy_name = '-DE_rand_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy3)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy3,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy3,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)



strategy_name = '-DE_best_2'
DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy4)
DSIDE_obj.optimize(filename='DSIDE_2-3line1'+strategy_name,cr=0.4,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line2'+strategy_name,cr=0.6,sf=0.5)
DSIDE_obj.optimize(filename='DSIDE_2-3line3'+strategy_name,cr=0.8,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy4,cr_fix=False,control=True)
DSIDE_obj.optimize(filename = 'DSIDE_2-3line4'+strategy_name,sf=0.5,cr_reversed=True)
DSIDE_obj.optimize(filename='DSIDE_2-3line5'+strategy_name,sf=0.5)

DSIDE_obj = DSIDE_Algorithm(functionname='Scaffer2',functioneveluate=Scaffer2_fun,functiontype='MultimodalFunction',strategy=strategy4,cr_fix=False)
DSIDE_obj.optimize(filename='DSIDE_2-3line6'+strategy_name,sf=0.5)