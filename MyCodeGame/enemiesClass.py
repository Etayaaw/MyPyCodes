import beautyOutput


class Enemy():
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.level = 1
        if race.lower() == 'skeleton':
            self.health = 70
            self.strength = 5
            self.agility = 30
        elif race.lower() == 'zombie':
            self.health = 100
            self.strength = 10
            self.agility = 15
        elif race.lower() == 'demon':
            self.health = 115
            self.strength = 15
            self.agility = 0
    
    def showEnemy(self):
        beautyOutput.printUnit('E', self.name, self.race, str(self.level), str(self.health), str(self.strength), str(self.agility))
    
    def levelUp(self):
        self.level += 1

    def strengthUp(self):
        self.strength += 1

    def agilityUp(self):
        self.agility += 1

    def setHealth(self, newHealth):
        if newHealth <= 0:
            Enemy.enemyDies(self)
        self.health = newHealth

    def enemyDies(self):
        self.health = 0
        print('[E]The Enemy ' + self.name + ' is Dead!')
    
    def escaped(self):
        self.health = 0