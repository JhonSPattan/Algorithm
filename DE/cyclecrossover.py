import numpy as np
import random
""" p1 = np.array([1,4,2,3,5])
p2 = np.array([2,3,5,1,4]) """
p1 = np.array([2,5,1,3,4])
p2 = np.array([4,1,5,2,3])
cycle = (np.ones(5))*-1

ch1 = (np.ones(5))*-1
ch2 = (np.ones(5))*-1
start_index = 4
myindex = start_index
#next_index1 = np.where(p1 == p2[0])[0][0]
#next_index2 = np.where(p2 == p1[0])[0][0]
count = 0
print(p1)
print(p2)

print('start at',start_index)

#build cycle

for i in range(5):
    """  if i == 0:
        cycle[i] = np.where(p1 == p2[i])[0][0]
        myindex =  cycle[i]
    else: """
    if start_index in cycle:
        continue
    cycle[i] = np.where(p1 == p2[np.int32(myindex)])[0][0]
    myindex = cycle[i]

        
        

print(cycle)

for i in range(5):
    cr_pop = random.uniform(0,1)
    if  i in cycle and cr_pop < 0.8:
       print(i,' is contain in cycle')
       ch1[i] = p2[i]
       ch2[i] = p1[i]
    else:
        ch1[i] = p1[i]
        ch2[i] = p2[i]

print("Before repair operation")
print(ch1)
print(ch2)
# repaire chromosome

for i in range(5):
    if ch1[i] == -1:
        ch1[i] = p1[i]
    
    if ch2[i] == -1:
        ch2[i] = p2[i]

print("Affter repair operation")
print(ch1)
print(ch2)