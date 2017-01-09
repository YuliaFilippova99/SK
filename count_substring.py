from random import *
import math
import numpy
def freq(letter,text):
    num = 0
    for i in range(len(text)):
        if text[i] == letter:
            num += 1
    return num
def pairs(toSearch,text):
    num = 0
    for i in range(len(text)-len(toSearch)+1):
        if text[i:i+len(toSearch)] == toSearch:
            num += 1
    return num
def mystruct(text):
    num = 0
    for i in range(len(text)):
        if text[i] == "A" and text[i+1] == "T":
            for j in range(i+1,len(text)-1):
                if text[j:j+2] == "GG":
                    num += 1
                    break
    return num
string = input(u"Введите строку: ")
print("C frequency:",freq("C",string))
print("G frequency:",freq("G",string))
print("AA frequency:",pairs("AA",string))
print("AT...GG frquency:",mystruct(string))