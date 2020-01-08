# Create a game with random numbers between 0 and 100 (range)
# where the nuber of guesses is 10
# where numbers < x are said to be cold
# and numbers > x are said
# outputs should be 1. when the game is over
# 2. the number of tries made by the user
# 3. the number of user guesses
# Also make a list of the numbers being guessed (arrays)

import random  # import random module

winning_number = random.randint(0,100)
print("winning_number", winning_number)

total_guesses = 10
guesses = []  # Sets an array where i can store user guess inputs
user_won = False
guesses_taken = 0

while guesses_taken < total_guesses and user_won != True:
    user_guess = int(input("Enter your guess: "))
    guesses.append(user_guess)
    guesses_taken += 1
    if user_guess == winning_number:
        user_won = True
        print("Congrats,you won!")
    elif user_guess >= winning_number - 5 and user_guess <= winning_number + 5:
        print("Hot")
    elif user_guess >= winning_number - 10 and user_guess <= winning_number + 10:
        print("Warm")
    else:
        print("Cold")

print("You took", guesses_taken)
print("Your guesses were: ")
print(guesses)
