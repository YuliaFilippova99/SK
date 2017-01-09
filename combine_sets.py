from random import *
import math

r = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
c = ["C","D","H","S"]
deck = []

for i in range(len(r)):
    for j in range(len(c)):
        deck.append(r[i]+c[j])
#1-пункт(создане колоды)
print("Deck: ",deck)

numC = []
for i in range(10):
    for j in range(10):
        for h in range(10):
            for k in range(10):
                numC.append(str(i)+str(j)+str(h)+str(k))
lC = []

for i in range(65,70):
    for j in range(65,70):
        lC.append(chr(i)+chr(j))
for i in range(1040,1050):
    for j in range(1040,1050):
        lC.append(chr(i)+chr(j))
signs = []
for i in range(len(numC)):
    for i in range(len(lC)):
        signs.append(numC[i]+lC[i])
#все знаки сгенерированны

possibleNums = [0,1,2,3,4,5,6]
combinations = []
Sum7 = 0
for i in range(len(possibleNums)):
    for j in range(len(possibleNums)):
        combinations.append(str(possibleNums[i]) +":"+ str(possibleNums[j]))
        if possibleNums[i] + possibleNums[j] == 7:
            Sum7 += 1
print("All combinations: ",combinations)
print("Number of combinations with sum = 7: ",Sum7)
