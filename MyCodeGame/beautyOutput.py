import tqdm
import time
from art import tprint
from colorama import Fore

def printLogo():
    print(Fore.LIGHTYELLOW_EX + '______________________________________________________________________________' + Fore.GREEN)
    tprint('\n  MyCodeGame')
    print(Fore.LIGHTYELLOW_EX + '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾' + Fore.WHITE)

def printMainMenu():
    print(Fore.RED + ' [' + Fore.WHITE + '1' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + '  START   ' + Fore.RED + ' [' + Fore.WHITE + '1' + Fore.RED + '] ')
    print(' [' + Fore.WHITE + '2' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + ' TUTORIAL ' + Fore.RED + ' [' + Fore.WHITE + '2' + Fore.RED + '] ')
    print(' [' + Fore.WHITE + '3' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + '   EXIT   ' + Fore.RED + ' [' + Fore.WHITE + '3' + Fore.RED + '] ' + Fore.WHITE)

def printStart():
    print(Fore.LIGHTYELLOW_EX + '_______________________________________________________________________________________________' + Fore.GREEN)
    tprint('\n   TheGameStarts!')
    print(Fore.LIGHTYELLOW_EX + '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾' + Fore.WHITE)

def printTutorial():
    print(Fore.LIGHTYELLOW_EX + '______________________________________________________________________________' + Fore.GREEN)
    tprint('\n               Tutorial')
    print(Fore.LIGHTYELLOW_EX + '‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾' + Fore.WHITE)

def printUpgrades():
    print('         UPGRADE')
    print('__________________________')
    print(Fore.RED + '  [' + Fore.WHITE + '1' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + 'Health ' + Fore.LIGHTBLACK_EX + '(+25 HP)')
    print(Fore.RED + '  [' + Fore.WHITE + '2' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + 'Strength ' + Fore.LIGHTBLACK_EX + '(+1)')
    print(Fore.RED + '  [' + Fore.WHITE + '3' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + 'Agility ' + Fore.LIGHTBLACK_EX + '(+1)' + Fore.WHITE)
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
def printMenuDiscription():
    print('___________________________________________________________')
    print(' 1 - Hit Your Enemy! But Be Careful, He Will Strike Back.')
    print(' 2 - Block the Enemy Hit And Drink Health Potion!')
    print(' 3 - Try To Run Away, But Know That You Can Be Intercepted!')
    print(' 4 - Show Your Hero Stats')
    print(' 5 - Show Enemy Stats')
    print(" 'Menu' - To Bring Up That Menu Again")
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

def printMenu():
    print(Fore.YELLOW + '|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|')
    print('|' + Fore.RED + '  [' + Fore.WHITE + '1' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Damage              ' + Fore.YELLOW + '|')
    print('|' + Fore.RED + '  [' + Fore.WHITE + '2' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Block and Heal      ' + Fore.YELLOW + '|')
    print('|' + Fore.RED + '  [' + Fore.WHITE + '3' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Try to Leave        ' + Fore.YELLOW + '|')
    print('|' + Fore.RED + '  [' + Fore.WHITE + '4' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Show My Hero        ' + Fore.YELLOW + '|')
    print('|' + Fore.RED + '  [' + Fore.WHITE + '5' + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Show Enemy          ' + Fore.YELLOW + '|')
    print('|__________________________|' + Fore.WHITE + '')

def printUnit(letter, name, race, level, health, strength, agility):
    print(Fore.RED + ' [' + Fore.WHITE + letter + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Name:\t' + Fore.WHITE + name)
    print(Fore.RED + ' [' + Fore.WHITE + letter + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Race:\t' + Fore.WHITE + race)
    print(Fore.RED + ' [' + Fore.WHITE + letter + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' LVL:\t' + Fore.WHITE + level)
    print(Fore.RED + ' [' + Fore.WHITE + letter + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Health:\t' + Fore.WHITE + health)
    print(Fore.RED + ' [' + Fore.WHITE + letter + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Strength:\t' + Fore.WHITE + strength)
    print(Fore.RED + ' [' + Fore.WHITE + letter + Fore.RED + ']' + Fore.LIGHTGREEN_EX + ' Agility:\t' + Fore.WHITE + agility)

def printIncorrectRace():
    print(Fore.RED + ' [' + Fore.WHITE + '1' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + 'Try Again')
    print(Fore.RED + ' [' + Fore.WHITE + '2' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + 'Set Default ' + Fore.LIGHTBLACK_EX + '(Human)' + Fore.WHITE)

def printRace():
    print(Fore.RED + ' [' + Fore.WHITE + '1' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + 'Human' + Fore.LIGHTBLACK_EX + '  (Nothing Unusual)')
    print(Fore.RED + ' [' + Fore.WHITE + '2' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + 'Orc' + Fore.LIGHTBLACK_EX + '    (Strong and Clumsy)')
    print(Fore.RED + ' [' + Fore.WHITE + '3' + Fore.RED + '] ' + Fore.LIGHTGREEN_EX + 'Elf' + Fore.LIGHTBLACK_EX + '    (Weak but Smart)' + Fore.WHITE)

def doDelay(timeInSec = 1.0):
    time.sleep(timeInSec)

def printProgressBar(timeInMin = 0.1):
    data = range(100)
    for _ in tqdm.tqdm(data):
        time.sleep(timeInMin)

def printDottedBar(delayTimeInSec = 0.5, dotsAmount = 5):
    for _ in range(dotsAmount):
        print('.', end='')
        time.sleep(delayTimeInSec)
    print()

def printDots(delayTimeInSec = 1.0, dotsAmount = 3):
    for i in range(dotsAmount + 1):
        print('.' * i, end="\r")
        time.sleep(delayTimeInSec)
    print(end="\r")