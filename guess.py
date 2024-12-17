from random import randint
from art import logo

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(user_guess, actual_ans):
    if user_guess > actual_ans:
        print("Too High !")
    elif user_guess < actual_ans:
        print("Too Low !")

    

def set_dificulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard' : ")
    if level=="easy":
       return EASY_LEVEL_TURNS
       print("You have 10 attempts to guess the number. ")

    elif level=="hard":
        return HARD_LEVEL_TURNS
        print("You have 5 attempts to guess the number. ")
    else:
        print("Invalid choice. Please choose 'easy' or 'hard' ")



def game():

    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100.")
    answer=randint(1,100)

    #print(f"the correct answer is {answer}")

    turns=set_dificulty()
    while turns > 0:
        print(f"You have {turns} attempts to guess the number. ", )
        
        guess=int(input("Make a guess: "))
        check_answer(guess, answer)

        if guess==answer:
            print(f"Correct! The number was {answer}")
            return

        turns=turns-1

        if turns == 0:
            print("You have run out of guesses, you lose! ")
            print(f"The number was {answer}")
            return


game()