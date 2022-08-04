# import sys
# #main_path= 'C:/Users/patip/Documents/Python/StandartAlgorithm'
# #main_path = '/home/pythonrunnew/StandartAlgorithm'
# main_path = '/myweb/www/pythonrunnew/StandartAlgorithm'

# sys.path.insert(0,main_path)
# from AdptiveDSIDE import DSIDEclustering
# from Benchmark.functionbenchmark import Sphere

# Sphere_obj = DSIDEclustering(functioneveluate=Sphere,functionname='Sphere',lowerbound=-100,upperbound=100,round=30)
# Sphere_obj.optimize(filename='DSIDE-Kmean')


x = 35
y = 0

if(x%y == 0):
    print("Mod ok")
elif(x%y != 0):
    print("Can't mod")
elif(x == 0 or y == 0):
    print("some number is zero")