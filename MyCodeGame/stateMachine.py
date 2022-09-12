import heroesClass
import enemiesClass
import beautyOutput
import generator
import sys
import os


def clearConsole():
    os.system('cls')
    beautyOutput.printLogo()


def startTheGame():
    beautyOutput.printProgressBar(0.03)
    beautyOutput.printStart()
    print('____________________')
    print('Welcome to The Game!')
    print("Let's Create a Hero!")
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    myHero = heroesClass.Hero()
    beautyOutput.printDots(0.5, 5)
    print('__________________')
    print('Here is Your Hero:')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    myHero.showHero()
    print('____________')
    print("Let's Start!")
    print('‾‾‾‾‾‾‾‾‾‾‾‾')
    while myHero.health > 0:
        myHero.walkHero()
        print('_______________________')
        print('You Have Met The Enemy!')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        myEnemy = enemiesClass.Enemy(generator.generateName(), generator.generateRace())
        myEnemy.showEnemy()
        print()
        beautyOutput.printMenu()
        n = '0'
        while myEnemy.health > 0 and myHero.health > 0:
            n = input('> ')
            if n == '1':
                myHero.doDamage(myEnemy)
            elif n == '2':
                myHero.doBlockAndHeal(myEnemy)
            elif n == '3':
                myHero.doLeave(myEnemy)
            elif n == '4':
                myHero.showHero()
            elif n == '5':
                myEnemy.showEnemy()
            elif n.lower() == 'menu':
                beautyOutput.printMenu()
            else:
                print('Incorrect Input!')
        if myEnemy.health <= 0:
            print('The Enemy ' + myEnemy.name + ' Died!\n')
            print('___________________________')
            print('You Get Healed! (+25 HP)')
            print('Also You Get Upgrade Point!')
            print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
            myHero.setHealth(myHero.health + 25)
            myHero.levelUp()
            beautyOutput.printUpgrades()
            k = ''
            while k != '1' and k != '2' and k != '3':
                k = input('> ')
                if k == '1':
                    myHero.setHealth(myHero.health + 25)
                elif k == '2':
                    myHero.strengthUp()
                elif k == '3':
                    myHero.agilityUp()
                else:
                    print('Incorrect Input! Try Again...')
    if myHero.health <= 0:
        print('__________________________________')
        print('            Game Over!')
        print('Unfortunately, Your Hero Has Died.')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        temp = input('Press Enter to Exit to The Main Menu...')
        main()
    else: 
        print('Unexpected Error!')
        temp = input('Press Enter to Exit to The Main Menu...')
        main()

def goThroughTutorial():
    beautyOutput.printProgressBar(0.01)
    beautyOutput.printTutorial()
    print('_________________________________________')
    print('Welcome to the Game!')
    print('You Need to Create a Hero First!')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    myHero = heroesClass.Hero()
    beautyOutput.printDots(0.5, 5)
    print('__________________')
    print('Here is Your Hero:')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    myHero.showHero()
    print('_____________________________________________________')
    print('Since You Have a Hero, You Need to Accompany The Hero')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    temp = input('Press Enter to Continue...')

    print()
    myHero.walkHero()
    print('_______________________')
    print('Look! Your First Enemy!')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    myEnemy = enemiesClass.Enemy('Boneshaker', 'Skeleton')
    beautyOutput.doDelay(2)
    myEnemy.showEnemy()
    print('_____________________________________________________')
    print('Skeletons Are Weak, But Very Dexterous. Be Careful!')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    temp = input('Press Enter to Continue...')

    beautyOutput.printMenuDiscription()
    beautyOutput.doDelay(5)
    print('     Choose What to Do!')
    beautyOutput.printMenu()
    
    n = '0'
    while myEnemy.health > 0 and myHero.health > 0:
        n = input('> ')
        if n == '1':
            myHero.doDamage(myEnemy)
        elif n == '2':
            myHero.doBlockAndHeal(myEnemy)
        elif n == '3':
            myHero.doLeave(myEnemy)
        elif n == '4':
            myHero.showHero()
        elif n == '5':
            myEnemy.showEnemy()
        elif n.lower() == 'menu':
            beautyOutput.printMenu()
        else:
            print('Incorrect Input!')

    if myHero.health <= 0:
        print('________________________________________________')
        print('You Died Somehow... However, Tutorial Completed.')
        print('Now You Now How to Play The Game!')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        temp = input('Press Enter to Exit to The Main Menu...')
        main()
    elif myEnemy.health <= 0:
        print('The Enemy ' + myEnemy.name + ' Died!\n')
        print('___________________________')
        print('You Get Healed! (+25 HP)')
        print('Also You Get Upgrade Point!')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        myHero.setHealth(myHero.health + 25)
        myHero.levelUp()
        beautyOutput.printUpgrades()
        k = ''
        while k != '1' and k != '2' and k != '3':
            k = input('> ')
            if k == '1':
                myHero.setHealth(myHero.health + 25)
            elif k == '2':
                myHero.strengthUp()
            elif k == '3':
                myHero.agilityUp()
            else:
                print('Incorrect Input! Try Again...')
        print('________________________________________________________________')
        print('The Enemy is Dead! Congratulations! However, Tutorial Completed.')
        print('Now You Know How to Play The Game!')
        print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        temp = input('Press Enter to Exit to The Main Menu...')
        main()
    else: 
        print('Unexpected Error!')
        temp = input('Press Enter to Exit to The Main Menu...')
        main()

def exitFromGame():
    print('___________________')
    print('Thanks For Playing!')
    print('    Goodbye!')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    beautyOutput.printDottedBar(0.5, 5)
    sys.exit()


def main():
    command = ''
    clearConsole()
    beautyOutput.printMainMenu()
    while command != '1' and command != '2' and command != '3':
        command = input('> ').strip()
        if command != '1' and command != '2' and command != '3':
            print('Incorrect input! Try again...')
            continue
        if command == '3':
            exitFromGame()
        if command == '2':
            goThroughTutorial()
        if command == '1':
            startTheGame()