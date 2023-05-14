#print logo
from art import logo
print(logo)
#Generate comparison: Compare: A {X}, occupation, nationality)
from game_data import data
import random

# Function returns random account
def random_account():
    """Returns random instagram account from 'data' array"""
    return random.choice(data)

# Assign accounts to variables to be compared
account_a = random_account()
account_b = random_account()

# Make sure we aren't comparing an account to itself
while account_a == account_b:
    account_b = random_account()

print(account_a)
print(account_b)

#print vs
#Against B: {Y}, occupation, nationality
#Ask: WHo has more followers? input 
#Compare followers of A and B, compare input with right answer. 
# 
    # If answer is right, print: You're right! current score:. make B (person with less followers) = input and generate new comparison. 
    #If answer is wrong, end game. Display score and msg.
