from random import *
import math
import matplotlib.pyplot as plt
def piL(n):
    s = 0
    for i in range(n):
        s += float(1)/float(((4*i+1)*(4*i+3)))
    return 8*s

def piE(n):
    s = 0
    for i in range(1,n):
        s += float(1)/float(i**2)
    s *= 6
    return math.sqrt(s)

N = int(input(u"Input N > 1 = "))
rL = []
rE = []
nums = []
for i in range(1,N+1):
    nums.append(i)
    rL.append(math.fabs(piL(i)-math.pi))
    rE.append(math.fabs(piE(i)-math.pi))
plt.plot(nums,rL)
plt.plot(nums,rE)
plt.xlabel("N")
plt.ylabel("Radius")
plt.show()