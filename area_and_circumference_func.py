import math
 
def figure(a):
        a = float(a)
        s = math.pi * a**2
        print("Площадь круга ", s)
   
r = input("Введите радиус: ")
figure(r)