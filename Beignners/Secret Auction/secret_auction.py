__author__ = "Vineet Chhabra"

import os
from art import logo

print(logo)
bids = {}
print("Welcome to the secret auction program")
bidding_finished = False


def highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for i in bidder_record:
        bid_amount = bidder_record[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? \n").lower()
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
