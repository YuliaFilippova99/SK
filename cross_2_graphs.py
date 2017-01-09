import math
import numpy
def f(x):
    return x
def g(x):
    return x**2
def gf(x,e):
    d = []
    for i in range(len(x)):
        if math.fabs(f(x[i])-g(x[i])) < e:
            d.append(x[i])
    return d
n = int(input(u"Enter N = "))
eppsilon = float(input(u"Enter eppsilon = "))
s = [-4,4]
x = numpy.linspace(-4,4,n)
print("X = ",gf(x,eppsilon))