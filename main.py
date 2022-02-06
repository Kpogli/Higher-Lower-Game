import os
import random
from game_data import data
from art import logo, vs

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls.
        command = 'cls'
    os.system(command)

def format_data(account):
    """Takes the account data and returns printable formats"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}."

def check_answer(guess, a_follower_count, b_follower_count):
    """Takes user guess and follower counts and returns if user is correct."""
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

#Display Art.
print(logo)

#Initial score set.
score = 0

#Flag to keep the game alive.
game_should_continue = True

#Initial setting of account B
account_b = random.choice(data)

#Make the game repeatable, but make the account B become account A.
while game_should_continue:

    #Generate random account B again after setting account A to initially set account B
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask user for a guess.
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    #Check if user is correct.
    ##Get follow count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    ##Check if user is correct using check function defined earlier.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Clear the screen between rounds.
    clearConsole()
    print(logo)

    ##Give user feedback.
    ##Score keeping.
    if is_correct:
        score += 1
        print(f"\nYou are right!. Current score is {score}.\n")
    else:
        game_should_continue = False
        print(f"You got it wrong boi!!. Final score is {score}.")