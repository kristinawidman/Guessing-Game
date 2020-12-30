"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import math

print("=====>Welcome to Widman's Number Guessing Game!<=====")

name = input("What is your name? ")
 
    
def start_game():

    solution_num = random.randint(0,10) 
    counter = 1
    high_score = []
    # write your code inside this function.
    
    while True:    
         #need to loop back up to guess_attempt if they do not get the correct answer
        #if player guesses too high prompt them with a hint plus another guess
        guess_attempt = int(input("{}, guess a number between 1-10: ".format(name)))
        if guess_attempt > solution_num:
            print("It's lower. Try it again, {}! ".format(name))
            counter += 1
            continue
        
        #if player guesses too low prompt them with a hint plus another guess
        elif guess_attempt < solution_num:
            print("It's higher. Try it again, {}!".format(name))
            counter += 1
            continue
            
            #add to the counter when the guess is incorrect
        #if player gueses it correctly inform them Got it! and show attempts it took to get correct
        else:
            print("You Guessed It!" + " It took you {} times.".format(counter))
            new_round = input("Do you want to play the game again? Yes/No ")
            new_high_score = high_score.append(counter)
            
            if new_round.lower() != 'no':
                start_game() 
            #let player know game is ending or over
            else:
                print("Thanks for playing {}! Hope to see you again soon!".format(name))
            break
            
# Kick off the program by calling the start_game function.
start_game()

"""
TODO for Krista's overachieving game:
-figure out how to store a high score
-figure out how to print the high score when the game is called for a new round
-figure out how to store the high score unless someone does better
"""
 
            