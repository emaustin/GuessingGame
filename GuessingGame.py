#Number guessing game. Player has 5 guesses to get the correct number. 

import random

#clear_output only used in jupyternotebook
#from IPython.display import clear_output

##
## Function will continue to ask the user for a number between 1-100 until they either guess
##   the correct number or reach the maximum number of guesses. 
##
def ask():
    keepgoing = True
    guesscounter = 0
    while keepgoing:
        while True:
            try:
                guess = int(input("Guess a number between 1-100. You have {} guesses remaining.".format(5-guesscounter)))
                break
            except:
                print("Not a valid entry. Please enter a number.")
        if guesscounter <4 and guess != number:
            guesscounter += 1
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
        elif guess == number:
            print("Yay! You guessed it!")
            keepgoing = False
        else:
            print("You ran out of guesses! The correct number was {}".format(number))
            keepgoing= False


##
## Gets random number, runs the ask function, then checks to see if the user wants to play again.
##
playagain = True
while playagain:
    #get new random number
    number = random.randrange(1,101)
    ask()
    answer = input("Do you want to play again? Y/N")
    #replacing clear_output with an empty line print for the cmd line console
    #clear_output()
    print('\n'*25)
    if answer.upper() == 'Y':
        playagain = True
    elif answer.upper() == 'N':
        print("Thanks for playing!")
        playagain = False
