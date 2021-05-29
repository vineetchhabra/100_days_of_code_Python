from art import logo
import random
import os

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "LOSE, Opponent has BlackJack!!"
    elif user_score == 0:
        return "Win with a BlackJack!!"
    elif user_score > 21:
        return "You went over. You LOSE!!"
    elif computer_score > 21:
        return "Opponent went over. You Win!!"
    elif user_score > computer_score:
        return "You Win!!"
    else:
        return "You Lose!!"

def play_game():

    user_card = []
    computer_card = []
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(logo)
        print(f"    Your cards: {user_card}, Current Score: {user_score}")
        print(f"    Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:  ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"    Your final hand: {user_card}, Final Score: {user_score}")
    print(f"    Computer's final hand: {computer_card}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n':  ") == 'y':
    os.system('cls')
    play_game()