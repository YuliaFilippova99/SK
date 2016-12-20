import math

def polyarea(x,y):
     A = 0
    l = len(x)
    for i in range(l):
        if i+1 < l:
            A += (x[i]+x[i+1])*(y[i]-y[i+1])
        else:
            A += (x[i]+x[0])*(y[i]-y[0])
    return A/2

x = [1,1,3,3]
y = [1,3,3,1]
A = polyarea(x,y)

print("Площадь фигуры - ", A)

