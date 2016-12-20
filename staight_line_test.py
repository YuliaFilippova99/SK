from random import *
import math
import numpy

def function(x):
    return 4*x+1
def check(b):
    for i in range(1,len(b)+1):
        a = ((function(b[i-1])-function(c)))/(b[i-1]-c)
        if a == 4:
            print("for point ",i,"carry out: ",a," = ",tg)

tg = 4
i1 = int(input(u"Enter begin of fraction: "))
i2 = int(input(u"Enter end of fraction: "))
r = numpy.linspace(i2,i2,100)
c = 2

check(r)
