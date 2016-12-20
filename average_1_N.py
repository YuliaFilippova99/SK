import math

def average(N):
    a = 0
    for i in range(1,N+1):
        a += i
    return a/N

N = int(input(u"Enter number N > 1: "))
print("Average in [ 1,",N,"] = ",average(N))

