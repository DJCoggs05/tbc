# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:02:06 2024

@author: cough
"""
import random

class Character(object):
    def __init__(self):
        self.name = "Anonymous"
        self.hitPoints = 20
        self.hitChance = 50
        self.maxDamage = 5
        self.armor = 1
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
            
    @property
    def hitPoints(self):
        return self.__hitPoints
        
    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__hitPoints = value
            
    def testInt(self, value, min=0, max=100, default=0):
        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
        
        return out
        
    @property
    def hitChance(self):
        return self.__hitChance
        
    @hitChance.setter
    def hitChance(self, value):
        value = self.testInt(value, 0, 100, 0)
        self.__hitChance = value

    @property
    def maxDamage(self):
        return self.__maxDamage
        
    @maxDamage.setter
    def maxDamage(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__maxDamage = value
        
    @property
    def armor(self):
        return self.__armor
        
    @armor.setter
    def armor(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__armor = value
            
    def printStats(self):
        print(f"""
{self.name}
    Character Hit Points: {self.hitPoints}
    Character Hit Chance: {self.hitChance}
    Character Max Damage: {self.maxDamage}
    Character Armor: {self.armor}
""")


    def hit(self, opponent):
        randomChance = random.randint(1, 100)
        if randomChance <= self.hitChance:
            randomDamage = random.randint(1, self.maxDamage)
            randomDamage = randomDamage - opponent.armor
            print(f"{self.name} hits {opponent.name} for {randomDamage} damage!")
            opponent.hitPoints -= randomDamage 
            if opponent.hitPoints <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print(f"{self.name} misses the attack!")
def fight(playerOne, playerTwo):
    keepGoing = True
    while keepGoing:
        play = input("""
Press Enter to Attack
""")
        if play == "":
            playerOne.hit(playerTwo)
            playerTwo.hit(playerOne)
            if playerOne.hitPoints <= 0:
                keepGoing = False
                print(f"{playerOne.name} Has Lost!")
            elif playerTwo.hitPoints <= 0:
                keepGoing = False
                print(f"{playerTwo.name} Has Lost!")

def main():
    playerOne = Character()
    playerTwo = Character()
    
    playerOne.name = "George"
    playerOne.printStats()
    
    playerTwo.name = "Bob"
    playerTwo.printStats()

    fight(playerOne, playerTwo)
if __name__ == "__main__":
    main()