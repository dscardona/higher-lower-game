#print logo
from art import logo, vs
from game_data import data
import random

print(logo)

# Function returns random account
def random_account():
    """Returns random instagram account from 'data' array"""
    return random.choice(data)

#Define function to compare amount of followers of two accounts
def least_followers(accout_a, account_b):
    """Accepts two dictionaries (accounts), and outputs account with lower 'follower_count' value"""
    if account_a["follower_count"] > account_b["follower_count"]:
        return account_b
    elif account_a["follower_count"] < account_b["follower_count"]:
        return account_a
    else:
        return 0



# Assign accounts to variables to be compared
account_a = random_account()
account_b = random_account()

# Make sure we aren't comparing an account to itself
while account_a == account_b:
    account_b = random_account()

#Generate comparison then print: Compare: A {X}, occupation, nationality)
print(f"Comprare: A. {account_a['name']}, a(n) {account_a['description']}, from {account_a['country']}")
#print vs
print(vs)
#Against B: {Y}, occupation, nationality
print(f"Against: B. {account_b['name']}, a(n) {account_b['description']}, from {account_b['country']}")

#Ask: WHo has more followers? input 
answer = input("Who has more followers? Type 'A' or 'B': " )

#Compare followers of A and B, compare input with right answer. 


    # If answer is right, print: You're right! current score:. make B (person with less followers) = input and generate new comparison. 
    #If answer is wrong, end game. Display score and msg.
