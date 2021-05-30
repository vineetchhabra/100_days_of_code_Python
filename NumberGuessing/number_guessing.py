import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

guessed_number = random.randint(1, 101)

# game_ = True


difficulty = input("Choose a difficulty. Type'easy' or 'hard': ").lower()

def number_guess_easy():
    """Logic for easy play"""
    easy = 10
    
    while easy != 0:
        print(f"You have {easy} attempts to guess the number")
        guess = int(input("Make a Guess: "))
        if guess < guessed_number and easy != 0:
            print("Too Low!!")
            easy -= 1
                # print(f"You have {easy} attempts left.")
        elif guess > guessed_number and easy != 0:
            print("Too High!!")
            easy -= 1
                # print(f"You have {easy} attempts left")
        else :
            print("You Guessed the correct number , Yay! You Win!!")
        
                    
    print("You are out of Luck!! You LOSE!")
    print(f"The Guessed number was: {guessed_number}")
    go_again = input("Do you want to play again? Type  'y' or 'n': ")
    if go_again == 'y':
        number_guess_easy()


def number_guess_hard():
    """Logic for hard level play"""
    hard = 5
    while hard != 0:
        print(f"You have {hard} attempts to guess the number")
        guess = int(input("Make a Guess: "))
        if guess < guessed_number and hard != 0:
            print("Too Low!!")
            hard -= 1
            # print(f"You have {easy} attempts left.")
        elif guess > guessed_number and hard != 0:
            print("Too High!!")
            hard -= 1
            # print(f"You have {easy} attempts left")
        else :
            print("You Guessed the correct number , Yay! You Win!!")

    print("You are out of Luck!! You LOSE!")
    print(f"The Guessed number was: {guessed_number}")
    go_again = input("Do you want to play again? Type 'y' or 'n': ")
    if go_again == 'y':
        number_guess_hard()

if difficulty == "easy":
    number_guess_easy()
else:
    number_guess_hard()