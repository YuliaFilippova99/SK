import random
import math

class Player:
    index = 0
    sum = 0
    lost = False
    def defaultCards(self):
        for i in range(2):
            toAdd = random.randint(1, 10)
            self.sum += toAdd
            print("Игрок под номером", self.index, " вытянул", toAdd)
        print("Игрок под номером", self.index, " набрал", self.sum)
    def addNumber(self):
        if input(u"Если хотите вытянуть еще одну карту,напишите \"Д\",в ином случае напишите \"Н\" : ") == "Д":
            toAdd = random.randint(1,10)
            print("Игрок под номером",self.index," вытянул",toAdd)
            self.sum += toAdd
            self.check()
    def check(self):
        if self.sum > 21:
            print("Игрок под номером",self.index," набрал",self.sum," очков и ПРОИГРАЛ!")
            self.lost = True
        else:
            print("Игрок под номером",self.index," набрал", self.sum)
            self.addNumber()
    def win(self):
        print("Игрок под номером",self.index," набрал", self.sum," и ПОБЕДИЛ!!!!!!")


numberOfPlayers = int(input(u"Введите количество игроков = "))
players = []
for i in range(numberOfPlayers):
    players.append(Player())
    players[i].index = i+1
    players[i].defaultCards()
    players[i].addNumber()
    print("\n")

bestPlayer = []
maxSum = 0
for i in range(len(players)):
    if players[i].lost == False and players[i].sum > maxSum:
        maxSum = players[i].sum

if maxSum == 0:
    print("Все игроки проиграли")
else:
    for i in range(len(players)):
        if players[i].sum == maxSum:
            players[i].win()