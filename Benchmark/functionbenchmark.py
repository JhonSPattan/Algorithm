from cmath import pi, sqrt
from operator import le
import numpy as np
import math
#%% Unimodal function
def Sphere(vector_eveluate:np.array)->np.double:
    vector_eveluate = np.power(vector_eveluate,2)
    function_result  = np.sum(vector_eveluate)
    return function_result

def Elliptic(vector_eveluate:np.array)->np.double:
    dimension = len(vector_eveluate)
    function_result = 0
    for i in range(dimension):
        function_result = function_result+pow(10,0-1/dimension-1)*pow(vector_eveluate[i],2)
    return function_result

def Bent_ciger(vector_eveluate:np.array)->np.double:
    function_result = pow(vector_eveluate[0],2)+pow(10,6)*Sphere(vector_eveluate=vector_eveluate)
    return function_result


def Sum_sqares(vector_eveluate:np.array)->np.double:
    function_result = 0
    for i in range(len(vector_eveluate)):
        function_result = function_result + (i+1)*pow(vector_eveluate[i],2)
    return function_result


def Discuss(vector_eveluate:np.array)->np.double:
    vector_sqre = np.power(vector_eveluate,2)
    return pow(10,6)*pow(vector_eveluate[0],2)+np.sum(vector_sqre)

def Differentpowers(vector_eveluate:np.array)->np.double:
    function_result = 0
    for i in range(len(vector_eveluate)):
        abs_value = abs(vector_eveluate[i])
        pow_value = 2+4*((i+1)-1/len(vector_eveluate)-1)
        function_result = function_result + math.pow(abs_value,pow_value)
    return function_result

def Zakharov(vector_eveluate:np.array)->np.double:
    pow_vector = np.power(vector_eveluate,2)
    vector_eveluate = vector_eveluate*0.5
    sum_vector = np.sum(vector_eveluate)
    function_result = np.sum(pow_vector)+pow(sum_vector,2)+pow(sum_vector,4)
    return function_result




#%% Multimodal function

def Bohchaevsky_2(vector_eveluate:np.array)->np.double:
    function_result = 0
    for i in range(len(vector_eveluate)-1):
        function_result = function_result + (vector_eveluate[i]**2+2*vector_eveluate[i+1]**2-0.3*math.cos(3*pi*vector_eveluate[i])*math.cos(3*pi*vector_eveluate[i+1])+0.3)
    
    return function_result


def Rosenbrock(vector_eveluate:np.array)->np.double:
    #-30,30
    function_result = 0
    for i in range(len(vector_eveluate)-1):
        function_result = function_result + 100*pow((pow(vector_eveluate[i],2)-vector_eveluate[i+1]),2)+pow((vector_eveluate[i]-1),2)
    return function_result

def Griewank(vector_eveluate:np.array)->np.double:
    #-600,600
    function_result1 = 0
    function_result2 = 0
    for i in range(len(vector_eveluate)):
        function_result1 = function_result1+math.pow(vector_eveluate[i],2)
        function_result2 = function_result2*(math.cos(vector_eveluate[i]/math.sqrt(i+1))+1)
    return function_result1+function_result2

def Salomon(vector_eveluate:np.array)->np.double:
    Sphere_value = Sphere(vector_eveluate=vector_eveluate)
    Sphere_value = math.sqrt(Sphere_value)
    #print(Sphere_value)
    function_result = 1-math.cos(2*3.14*Sphere_value)+0.1*Sphere_value
    return function_result


def Scaffer2(vector_eveluate:np.array)->np.double:
    function_result = 0
    x = len(vector_eveluate)-1
    for i in range(len(vector_eveluate)-1):
        function_result = function_result + math.sqrt(vector_eveluate[i]*vector_eveluate[i]+vector_eveluate[i+1]*vector_eveluate[i+1])+(math.sin(50*pow(vector_eveluate[i]*vector_eveluate[i]+vector_eveluate[i+1]*vector_eveluate[i+1],0.1))+1)

    function_result = function_result + math.sqrt(vector_eveluate[x]*vector_eveluate[x]+vector_eveluate[0]*vector_eveluate[0])+(math.sin(50*pow(vector_eveluate[x]*vector_eveluate[x]+vector_eveluate[0]*vector_eveluate[0],0.1))+1)
    return function_result

def Weierstrass(vector_eveluate:np.array)->np.double:
    # -0.5,0.5
    function_result = 0
    a,b,k = 0.5,3,20
    size = len(vector_eveluate)
    for i in range(size):
        result1,result2 = 0,0
        for j in range(0,k+1):
            result1 = result1 + (math.pow(a,j))*(math.cos(2*math.pi*math.pow(b,j)*(vector_eveluate[i]+0.5)))
            result2 = result2 + (math.pow(a,j))*(math.cos(2*math.pi*math.pow(b,j)*(vector_eveluate[i]*0.5)))
        function_result = function_result + (result1-size*result2)
    
    return function_result

def Scaffer_F6(vector_eveluate:np.array)->np.double:
    function_result = 0
    for i in range(len(vector_eveluate)):
        sqare_value = 0
        if i+1 == len(vector_eveluate):
            sqare_value = math.pow(vector_eveluate[i],2)+math.pow(vector_eveluate[0],2)
        else:
            sqare_value = math.pow(vector_eveluate[i],2)+math.pow(vector_eveluate[i+1],2)

        sineValue = math.sin(math.sqrt(sqare_value))
        function_result = function_result+0.5+((math.pow(sineValue,2)-0.5)/math.pow((1+0.001*sqare_value),2))
    return function_result



#%% Asymmetric Multimodal function


def HappyCat(vector_eveluate:np.array)->np.double:
    size = len(vector_eveluate)
    sum_diff = 0
    for i in range(size):
        sum_diff = sum_diff+math.pow(vector_eveluate[i],2)-size
    sum_diff = math.pow(abs(sum_diff),0.25)
    sum_sqare = np.sum(vector_eveluate**2)
    sum_original = np.sum(vector_eveluate)

    function_result = sum_diff+(0.5*sum_sqare+sum_original)/size+0.5
    return function_result


def HGBat(vector_eveluate:np.array)->np.double:
    sum_eveluate = np.sum(vector_eveluate)
    sum_sqare = np.sum(vector_eveluate**2)
    function_result = abs(sum_sqare**2 - sum_eveluate**2)**0.5 +( (0.5*sum_sqare+sum_eveluate)/len(vector_eveluate))+0.5
    return function_result


def Whitley(vector_eveluate:np.array)->np.double:
    dimension = len(vector_eveluate)
    function_result = 0
    for i in range(dimension):
        for j in range(dimension):
            front = 100*math.pow(math.pow(vector_eveluate[i],2)-vector_eveluate[j],2)
            back = math.pow(1-vector_eveluate[j],2)
            function_result = function_result + (math.pow(front+back,2)/4000 - math.cos(front+back)+1)
    return function_result

# for Penalized and Penalized2
def u_function(x:float,a:float,k:float,m:float): 
    if x > a:
        return k*math.pow((x-a),m)
    elif x >= -a and x <= a:
        return 0
    elif x < -a:
        return k*math.pow((-x-a),m)

def y_calculation(x:float):
    return 1+((x+1)/4)

def Penalized(vector_eveluate:np.array)->np.double:
    dimension = len(vector_eveluate)
    y1_val = 10*math.sin(math.pi*y_calculation(vector_eveluate[0]))
    yn_val = math.pow(y_calculation(vector_eveluate[dimension-1])-1,2)
    sum_val1 = 0
    sum_val2 = 0
    u_val = 0
    for i in range(0,dimension-1):
        sum_val1 = sum_val1+math.pow(y_calculation(vector_eveluate[i])-1,2)
    
    for i in range(0,dimension-1):
        sum_val2 = (1+10*math.sin(math.pi*y_calculation(vector_eveluate[i+1]))**2)

    for i in range(dimension):
        u_val = u_val + u_function(vector_eveluate[i],10,100,4)
    function_result = (math.pi/dimension)*(y1_val+(sum_val1*sum_val2)+yn_val)
    function_result = function_result+u_val

    return function_result

    





