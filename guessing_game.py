"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import math

print("=====>Welcome to Widman's Number Guessing Game!<=====")

solution_num = random.randint(0,10)    


    
def start_game():

    
    counter = 1
    # write your code inside this function.
    name = input("What is your name? ")
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
            print("You Guessed It!" + " It took you {} times.".format( counter))
            new_round = input("Do you want to play the game again? Yes/No ")
            if new_round.lower() != 'no':
                continue 
            else:
                print("Thanks for playing {}! Hope to see you again soon!".format(name))
            break

            
    
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
            