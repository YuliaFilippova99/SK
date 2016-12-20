import math
from random import *
x = []
#Пузырьковая сортировка
def sorting(x):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                a = x[i]
                x[i] = x[j]
                x[j] = a
return x
for i in range(6):
x.append(uniform(0,10))
print(x)
print(sorting(x))
