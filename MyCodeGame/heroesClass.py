import beautyOutput
from random import randrange


class Hero():
    def __init__(self):
        self.level = 1
        name = ''
        print('Enter The Name For Your Hero...')
        while name == '' or len(name) < 2:
            name = input('> ').strip().lower().capitalize()
            if name == '':
                print('Incorrect Name! Try Again...')
                continue
            if len(name) < 2:
                print('Name is Too Short! Minimum 2 Symbols. Try Again...')
                continue
        self.name = name

        print('Choose The Race For Your Hero...')
        beautyOutput.printRace()
        race = ''
        while race != '1' and race != '2' and race != '3':
            race = input('> ')
            if race == '1':
                self.race = 'Human'
                self.health = 100
                self.strength = 10
                self.agility = 15
                print('Race is Set to Human')
            elif race == '2':
                self.race = 'Orc'
                self.health = 120
                self.strength = 15
                self.agility = 5
                print('Race is Set to Orc')
            elif race == '3':
                self.race = 'Elf'
                self.health = 80
                self.strength = 8
                self.agility = 30
                print('Race is Set to Elf')
            else: print('Incorrect Input! Try Again...')

    def walkHero(self):
        print('The Hero ' + self.name + ' is Moving', end = '')
        beautyOutput.printDottedBar(1.5, 3)

    def showHero(self):
        beautyOutput.printUnit('H', self.name, self.race, str(self.level),
        str(self.health), str(self.strength), str(self.agility))
    
    def levelUp(self):
        self.level += 1

    def strengthUp(self):
        self.strength += 1
    
    def agilityUp(self):
        self.agility += 1

    def setHealth(self, newHealth):
        if newHealth <= 0:
            Hero.heroDies(self)
        self.health = newHealth

    def heroDies(self):
        self.health = 0
        print('[H]The Hero ' + self.name + ' is Dead!')
    
    def doDamage(self, enemy):
        chance = enemy.agility
        n = randrange(100)
        if n > chance:
            print(enemy.name + ' Took -' + str(self.strength) + 'HP')
            enemy.setHealth(enemy.health - self.strength)
            print(enemy.name + "'s HP: " + str(enemy.health))
        else:
            print(enemy.name + ' Dodged a Punch!')
        if enemy.health > 0:
            beautyOutput.printDots(0.3, 3)
            chance = self.agility
            n = randrange(100)
            if n > chance:                  
                self.setHealth(self.health - enemy.strength)
                print(enemy.name + ' Deal ' + str(enemy.strength) + ' Damage')
                print(self.name + "'s HP: " + str(self.health))
            else:
                print(self.name + ' Dodged a Punch!')
    
    def doLeave(self, enemy):
        chance = self.agility
        n = randrange(100)
        if n <= chance:
            enemy.escaped()
            print('Success!')
        else: 
            print('Escape Failed! Your Hero Took Double Damage')
            self.setHealth(self.health - (enemy.strength * 2))
            print(self.name + "'s HP: " + str(self.health))

    def doBlockAndHeal(self, enemy):
        self.setHealth((self.health - (enemy.strength // 2)))
        print('Your Hero Get ' + str(enemy.strength // 2) + ' Damage')
        chance = enemy.agility
        n = randrange(100)
        if n <= chance:
            self.setHealth(self.health + 25)
            print('Your Hero Also Heal 25 HP: ' + str(self.health))
        else:
            self.setHealth(self.health - (enemy.strength * 2))
            print(enemy.name + ' Interrupted Healing and Deal Double Damage')
            print(self.name + "'s HP: " + str(self.health))