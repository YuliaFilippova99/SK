import random
import math

N = int(input(u"Enter N: "))
M = 0
a = []
for i in range(N):
 a.append(random.randint(1,6))
    if a[i] == 6:
     M += 1
print("Numbers of 6:",M)
print("M/N: ",M/N)
if N <= 300000:   
print("Generated: \n",a)
