# This File holds functions used during the various tasks 
# In this Directory.

################################ Imports ################################

import os
import random
from time import sleep

################################ Task 3 ################################

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def displayWelcome():
    # Sets Welcome message & Prints
    welcome = '\t\tWelcome to the "Guess the Number" game by CodeWithCuesta!'
    welcome += '\nRules: Select a max number range and the CPU will generate a random number.\n'
    welcome += 'YOU then have to guess the number.'
    welcome += ' Too many guesses.. you lose! Guess right.. you win!\n'
    print(color.CYAN + 'CodeWithCuesta' + color.END)
    print (welcome)

def setRange():
    #Propmt user for input of range-max
    range_max = int(input('Determine max range of random number: '))
    global random_num 
    random_num = random.randint(1, range_max)
    print('Random CPU Number Range: 1 -', range_max)

def startGuessing():
    #Prompt user for 1st guess, repeat until right or out of guesses
    guess_count = 0
    while True:
        if guess_count == 4:
            print('\n\t\t*[Final Guess]*')
        guess = int(input('\nGuess an integer to identify the random number: '))
        if isinstance(guess, int):
            guess_count += 1
            if guess_count == 5:
                lose()
            print('\t\tTotal guesses: ', guess_count)
            print('\nValidating..........')
            sleep(1)
            print('\n.....Validating.....')
            sleep(1)
            print('\n..........Validating\n')
            sleep(1)
        else:
            print('Error: "' + guess + '" Not Recognized as an integer\n')
            print('Please enter valid number.\nTry Again, please.')
            exit()

        if guess < random_num:
            print('[Guess is Too Low!]')
            print('Your Guess: ', guess)
        elif guess > random_num:
            print('[Guess is Too high!]')
            print('Your Guess: ', guess)
        else: # If Guess EQUALS Random_num
            win()

def win():
    # Display Winning stuffs
    os.system('clear && neofetch')
    print(color.CYAN + 'CodeWithCuesta' + color.END)
    print(color.GREEN + '\n\t\tCongrats you have guessed the Random CPU generated number correct!' + color.END)
    print('Enjoy your Cake!\nThe correct answer was - ', random_num)
    print('\n')
    exit()

def lose():
    # Lose
    os.system('clear')
    print(color.YELLOW + '\t\t[Error you have used all your guesses!]\n' + color.END)
    print("Random Number CPU generated was: ", random_num)
    print('\t\t' + color.RED + 'You Lose!' + color.END)
    print("To play again, type this command: python3 task-3.py\n")
    print(color.CYAN + '\t\tCodeWithCuesta\n' + color.END)
    exit()


################################ Task 4 ################################

def getTerms():
    # Prompts user for number of terms 
    # Validates inttered term as int
    terms = int(input('How many Terms would you like to see?\nTerms: '))
    if isinstance(terms, int):
        sleep(1)
        print('\nValidating..........')
        sleep(1)
        print('\n..........Validating\n')
        sleep(1)
    else: 
        print(color.Yellow + 'Error: ' + terms + ' is not a valid Integer.')
        exit()
    print('Selected Terms -', terms)   
    terms = terms - 1 
    return terms

def getFib(num):
    fib = [0,1]
    global i
    i = 0
    while i < num:
        x = fib[i] + fib[i+1]
        fib.append(x)
        i += 1
    print('\nFibonacci Sequence:')
    print(fib)

################################ Task 5 ################################

def getText():
    # Prompts user for string of text
    text = input('Enter a sentence or passage to display its word count.\nText: ')
    return text

def getWordCount(string):
    # itterates over text/string counts spaces and produces word count
    wordCount = 1
    for x in string:
        if x == ' ':
            wordCount += 1
    return wordCount

################################ Task 6 ################################

def getTemp():
    # prompts user for temps and unit
    # appends to tempList if valid
    list = []
    print('Enter a temperature to be converted.')
    currentTemp = 'a'
    while not isinstance(currentTemp, int):
        try:
            currentTemp = int(input('\nCurrent Temp: '))
        except ValueError:
            print("Invalid input. Please enter a numeric integer value.")
    currentTemp = int(input('Current Temp: '))
    list.append(currentTemp)

    unitList = ['f', 'c']
    print('Now enter a unit for the current temp(F = Fahrenheit, C = Celcius)')
    unit = 1
    while not isinstance(unit, str):
        try:
            unit + str(input('\nCurrent Unit (F or C): '))
        except ValueError:
            print("Invalid input. Please enter a numeric integer value.")
    if unit.lower() in unitList:
        list.append(unit)
    return list

################################ Task ################################




