#print logo
from art import logo, vs
from game_data import data
import random
import os

print(logo)

# Function returns random account
def random_account():
    """Returns random instagram account from 'data' array"""
    return random.choice(data)

#Define function to return account with lower amt of followers
def less_followers(account_a, account_b):
    """Accepts two dictionaries (accounts), and outputs account with lower 'follower_count' value"""
    if account_a["follower_count"] > account_b["follower_count"]:
        return account_b
    elif account_a["follower_count"] < account_b["follower_count"]:
        return account_a


# Flag, turns game of when False
right_answer = True

# Keep track of score
score = 0

# Assign accounts to variables to be compared
account_a = random_account()
account_b = random_account()

#Keeps game going until right_answer = False
while right_answer:

    # Make sure we aren't comparing an account to itself
    while account_a == account_b:
        account_b = random_account()

    #Compare: A {X}, occupation, nationality
    print(f"Comprare: A. {account_a['name']}, a(n) {account_a['description']}, from {account_a['country']}")

    #print vs
    print(vs)

    #Against B: {Y}, occupation, nationality
    print(f"Against: B. {account_b['name']}, a(n) {account_b['description']}, from {account_b['country']}")

    #Ask: initialize variable with answer
    answer = input("Who has more followers? Type 'A' or 'B': " )
    if answer == 'A':
        answer = account_a
    elif answer == 'B':
        answer = account_b

    #Figure out what account has less followers, compare to answer
    lower_count_acct = less_followers(account_a, account_b)
    if lower_count_acct == answer:
        #If answer is wrong, end game. Display score and msg.
        print(f"You lose! Final score: {score}")
        right_answer = False
    else:
        # If answer is right, print: You're right! current score:. make person with less followers = input and generate new comparison. 
        score += 1
        os.system('clear')
        print(f"You're right! Current score: {score}\n\n")
        account_a = account_b
        account_b = random_account()
        