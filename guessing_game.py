"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import math


def add_counter(guess):
    counter += 1

    
solution_num = random.randint(0,20)

def start_game():

    # write your code inside this function.
    welcome = print("Welcome to Widman's Number Guessing Game!")
    name = input("What is your name? ")
    counter = 0

    while True:    
        guess_attempt = int(input("{}, guess a number between 1-20: ".format(name)))

         #need to loop back up to guess_attempt if they do not get the correct answer
        #if player guesses too high prompt them with a hint plus another guess
        if guess_attempt > solution_num:
            print("It's lower. Try it again, {}! ".format(name))
            continue
        
        #if player guesses too low prompt them with a hint plus another guess
        elif guess_attempt < solution_num:
            print("It's higher. Try it again, {}!".format(name))
            continue
            
            #add to the counter when the guess is incorrect
        #if player gueses it correctly inform them Got it! and show attempts it took to get correct
        else:
            print("You Guessed It!" + " It took you {} times".format(counter))
            break
            add_counter(guess_attempt)
            
    
            #let player know game is ending or over


            # Kick off the program by calling the start_game function.
start_game()
print(solution_num)




 
"""
Psuedo-code Hints
--------------------------------

3. Continuously prompt the player for a guess.
  a. If the guess greater than the solution, display to the player "It's lower".
  b. If the guess is less than the solution, display to the player "It's higher".

4. Once the guess is correct, stop looping, inform the user they "Got it"
     and show how many attempts it took them to get the correct number.
5. Let the player know the game is ending, or something that indicates the game is over.

( You can add more features/enhancements if you'd like to. )
"""
            