# Name: Nguyen Duy Khang

import random

def compareNum(number, answer, count):
    if (number == answer):
        print("Congratulations! You have correctly guess the number with "+str(guessTimes)+" guess left")
        return True
    elif (number > answer):
        print("Your guess is higher. You have "+str(guessTimes)+" guess left.")
        return False
    else:
        print("Your guess it lower. You have "+str(guessTimes)+" guess left.")
        return False

continueGame = True
guessTimes = 0

print("Welcome to my Guess the number Game!")
while (continueGame != False):
    correctNumber = random.randint(1,5)
    while True:
        gameModeInput = input("Choose your mode: E/e for easy - H/h for hard: ")
        gameMode = gameModeInput.lower()
        if (gameMode == "e"):
            print("You have 10 tries to guess the correct number.")
            guessTimes = 10
            break
        elif (gameMode == "h"):
            print("You have 5 tries to guess the correct number.")
            guessTimes = 5
            break
    while (guessTimes > 0):
        while True:
            playerGuessInput = input("Guess a number between 1 and 100: ")
            if (playerGuessInput.isdigit() == True):
                if (1 <= int(playerGuessInput) <= 100):
                    guessTimes -= 1
                    break
        playerGuessNumber = int(playerGuessInput)
        if(compareNum(playerGuessNumber, correctNumber, guessTimes) == True):
            guessTimes = 0
    while True:
        playerContinueInput = input("Would you like to continue the game? Y/y for yes - N/n for no: ")
        playerContinue = playerContinueInput.lower()
        if (playerContinue == "n"):
            continueGame = False
            break
        elif (playerContinue == "y"):
            continueGame = True
            break
        
    
    
