# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:20:58 2024

@author: cough
"""

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
        self.maxHealth = 20
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
        value = self.testInt(value, 0, 1000, 0, isHitPoints = True)
        self.__hitPoints = value
            
    def testInt(self, value, min=0, max=100, default=0, isHitPoints=False):
        out = default
    
        if type(value) == int:
            if value > 0 or not isHitPoints:
                if value >= min:
                    if value <= max:
                        out = value 
                    else:
                        print("Too large")
                else:
                    print("Too small")
            else:
                out = value
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
            
    @property
    def maxHealth(self):
        return self.__maxHealth
    
    @maxHealth.setter
    def maxHealth(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__maxHealth = value
    def printStats(self, showAllStats = False):
        if showAllStats:
            print(f"""
    {self.name}
        Health: {self.hitPoints}
        Hit Chance: {self.hitChance}
        Max Damage: {self.maxDamage}
        Armor: {self.armor}
    """)
        else:
            print(f"{self.name}: Health: {self.hitPoints}")



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
    poison_duration = 0
    poison_damage = 0
    
    while keepGoing:
        play = input("""
Please select an option:
1) Fight
2) Heal
3) Focus

""")

        if play == "1":
            playerOne.hit(playerTwo)
            randomAction = random.random()
            if randomAction <= 0.15:
                healingAmount = int(playerTwo.maxHealth * 0.1)
                playerTwo.hitPoints = min(playerTwo.hitPoints + healingAmount, playerTwo.maxHealth)
                print(f"{playerTwo.name} has healed for {healingAmount}!")
            elif randomAction <= 0.1:
                damageIncrease = int(playerTwo.maxDamage * 0.1)
                playerTwo.maxDamage = playerTwo.maxDamage + damageIncrease
                print(f"{playerTwo.name} has powered up!")
            elif random.random() <= 0.05:
                print(f"{playerTwo.name} has poisoned {playerOne.name}!")
                poison_duration = 3
            else:
                playerTwo.hit(playerOne)
                if poison_duration > 0:
                    poison_damage += 2
                
            playerOne.hitPoints -= poison_damage  # Apply poison damage
            poison_damage = 0  # Reset poison damage for next turn
            
            playerOne.printStats(showAllStats=False)
            playerTwo.printStats(showAllStats=False)
            if playerOne.hitPoints <= 0:
                keepGoing = False
                print(f"{playerOne.name} Has Lost!")
            elif playerTwo.hitPoints <= 0:
                keepGoing = False
                print(f"{playerTwo.name} Has Lost!")
                
        elif play == "2":
            healingAmount = int(playerOne.maxHealth * 0.1)
            playerOne.hitPoints = min(playerOne.hitPoints + healingAmount, playerOne.maxHealth)
            print(f"{playerOne.name} has healed for {healingAmount}!")
            playerOne.printStats(showAllStats=False)
            randomAction = random.random()
            if randomAction <= 0.15:
                healingAmount = int(playerTwo.maxHealth * 0.1)
                playerTwo.hitPoints = min(playerTwo.hitPoints + healingAmount, playerTwo.maxHealth)
                print(f"{playerTwo.name} has healed for {healingAmount}!")
            elif randomAction <= 0.1:
                damageIncrease = int(playerTwo.maxDamage * 0.1)
                playerTwo.maxDamage = playerTwo.maxDamage + damageIncrease
                print(f"{playerTwo.name} has powered up!")
            elif random.random() <= 0.05:
                print(f"{playerTwo.name} has poisoned {playerOne.name}!")
                poison_duration = 3
            else:
                playerTwo.hit(playerOne)
                if poison_duration > 0:
                    poison_damage += 2
                
            playerOne.hitPoints -= poison_damage  # Apply poison damage
            poison_damage = 0  # Reset poison damage for next turn
            
            playerOne.printStats(showAllStats=False)
            playerTwo.printStats(showAllStats=False)
            
        elif play == "3":
            playerOne.hitChance += 2
            print(f"{playerOne.name}'s Accuracy has Increased!")
            
            randomAction = random.random()
            if randomAction <= 0.15:
                healingAmount = int(playerTwo.maxHealth * 0.1)
                playerTwo.hitPoints = min(playerTwo.hitPoints + healingAmount, playerTwo.maxHealth)
                print(f"{playerTwo.name} has healed for {healingAmount}!")
            elif randomAction <= 0.1:
                damageIncrease = int(playerTwo.maxDamage * 0.1)
                playerTwo.maxDamage = playerTwo.maxDamage + damageIncrease
                print(f"{playerTwo.name} has powered up!")
            elif random.random() <= 0.05:
                print(f"{playerTwo.name} has poisoned {playerOne.name}!")
                poison_duration = 3
            else:
                playerTwo.hit(playerOne)
                if poison_duration > 0:
                    poison_damage += 2
                
            playerOne.hitPoints -= poison_damage  # Apply poison damage
            poison_damage = 0  # Reset poison damage for next turn
            
            playerOne.printStats(showAllStats=False)
            playerTwo.printStats(showAllStats=False)
            
        if poison_duration > 0:
            poison_duration -= 1
                
        else:
            continue

def main():
    playerOne = Character()
    playerTwo = Character()
    
    playerOne.name = "George"
    playerOne.printStats(showAllStats = True)
    
    playerTwo.name = "Bob"
    playerTwo.printStats(showAllStats = True)

    fight(playerOne, playerTwo)
    
if __name__ == "__main__":
    main()