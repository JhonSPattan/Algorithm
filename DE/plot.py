import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import sys
sys.path.insert(0,'C:/Users/patip/Documents/Python/Algorithm')
from Benchmark.functionbenchmark import Scaffer2 as Scaffer2_fun
from Benchmark.functionbenchmark import Scaffer_F6 as Scaffer_F6_fun
from Benchmark.functionbenchmark import Rosenbrock as Rosenbrock_fun
from Benchmark.functionbenchmark import Bohchaevsky_2 as Bohchaevsky_2_fun
from Benchmark.functionbenchmark import Penalized as Peanlized_fun
from Benchmark.functionbenchmark import Whitley as Whitley_fun
N = 100
x_values = np.linspace(-1.5,1,N)
y_values = np.linspace(-1.5,1,N)
X,Y = np.meshgrid(x_values,y_values) #mearge value x,y
Z = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        dummy = np.array([X[i][j],Y[i][j]])
        Z[i][j] = Rosenbrock_fun(dummy)

levels = np.linspace(np.min(Z), np.max(Z),5)
ax = plt.figure(figsize=(12,12))
ax = plt.axes(projection='3d')
#fig, ax = plt.subplots()
ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)
#ax.contour(X,Y,Z,levels=levels)
ax.set_title("Rosenbrock 3d chart")
plt.show()
#print(Z[0])