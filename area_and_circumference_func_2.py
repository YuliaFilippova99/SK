import math
def figureC(r):
    a = 2*math.pi*r
    print(a)
    return a

def figureA(r):
    return math.pi*r**2
r = input(u'Enter r: ')
C = figureC(int(r))
A = figureA(int(r))

print("Length: ", C,"\nArea:  ",A)