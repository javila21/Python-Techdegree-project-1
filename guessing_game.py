"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
        
import random
import sys
guess_list = []
interim_list = []
def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("-----------------------------")
welcome_message()
highs_score = (999)


while True:
    
    #Got help from Slack to find ".randint"
    random_number = random.randint(1,10)
    new_guess = int  
    
    def high_score():
        current_score = len(interim_list)
        if int(current_score) < highs_score:
            highest_score = len(interim_list)
        print("The HIGHSCORE is {}".format(highest_score))    
        random_number = random.randint(1,10)
        guess_list[:] = []
        #used stack over flow to find this method of clearing a list  
    
    
    def end_of_game():
        print("You got it! It took you {} tries.".format(len(guess_list)))
        play_again = input("Would you like to play again?[y]es/[n]o: ")
        if play_again == "y":
            interim_list.extend(guess_list)
            high_score()
        elif play_again == "n":
            print("Thank you for playing with us! See you next time.") 
            sys.exit()
        else:
            print("That is is not a valid value please use either y or n.")
            end_of_game()
#used stackoverflow to get sys.exit()   
    
    
    def higher_lower():
        if new_guess > 10:
            print("Value is out of range, pick a number less than 11")
        elif new_guess < 1:
            print("Value is out of range, pick a numberr higher than 0")
        elif new_guess > random_number:
            print("It is lower!")
        elif new_guess < random_number:
            print("It is higher!")
        
    
    while new_guess != random_number:
        try:
            new_guess = int(input("Pick a number between 1 and 10: "))
        except ValueError:  
            print("That was not a valid input. Please pick a number between 1 and 10")
        else:    
            guess_list.append(new_guess) 
            if new_guess == random_number:
                interim_list[:] = []
                end_of_game()
            elif new_guess != random_number:
                higher_lower()    
                
                
def start_game():

    if __name__ == '__main__':
        # Kick off the program by calling the start_game function.
        start_game()
