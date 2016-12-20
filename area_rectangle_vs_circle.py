import math

r = 10.6
a = 1.3
b = 0
s = math.pi * r**2
while True:
    b += 1
    if a*b >= r:
        b -= 1
        break
print(b)

