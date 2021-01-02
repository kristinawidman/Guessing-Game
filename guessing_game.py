"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import math

print("=====>Welcome to K-Widman's Number Guessing Game!<=====")

name = input("What is your name? ")
high_score = [] 
    
def start_game():

    solution_num = random.randint(1,10) 
    counter = 1
    
    # write your code inside this function.
    
    while True:    
        #need to loop back up to guess_attempt if they do not get the correct answer
        #if player guesses too high prompt them with a hint plus another guess
        
        try:
            guess_attempt = int(input("{}, guess a number between 1-10: ".format(name)))
        except ValueError:
            print("Ooops, try guessing a number between 1-10.")
            
        else:
            if guess_attempt > 10 or guess_attempt < 1:
                print("Try a number between 1-10")
                continue
                
            elif guess_attempt > solution_num:
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
                new_high_score = high_score.append(counter)
                
                while True:
                    new_round = input("Do you want to play the game again? Yes/No ")
                        
                    if new_round.lower() == 'yes':
                        print("Your high score is {}! See if you can beat it!".format(min(high_score)))
                        start_game()
                        
                    elif new_round.lower() != 'no':
                        print("Ooops, type yes or no to continue.")
                        continue
                        
                    #let player know game is ending or over
                    else:
                        print("Thanks for playing, {}! Hope to see you again soon!".format(name))
                        break
                    break
            break
                        
                    
                
#           
# Kick off the program by calling the start_game function.
start_game()

"""
TODO for Krista's overachieving game:
-Run this guessing game with Brad
-Possibly run this game with a friend. :)
"""
 
            