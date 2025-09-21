import time
import random
import os
import sys

# Intro
print("Number Game")
time.sleep(2)
print("You will try to guess the number that I have! (1 to 50)")
time.sleep(2)
print("Try to get the highest number of points!\n")
time.sleep(2)

num_list = list(range(1, 51))

def ask_question():
    """Ask the user for a valid guess."""
    while True:
        guessed = input("What number do you think it is? : ")
        if guessed.isdigit() and 1 <= int(guessed) <= 50:
            return int(guessed)
        print("Please enter a digit from 1 to 50!")

points = 0
LIVES_PER_ROUND = 5

while True:
    print("Generating Number...\n")
    time.sleep(2)
    generated = random.choice(num_list)
    lives = LIVES_PER_ROUND

    while lives > 0:
        guessed2 = ask_question()
        lives -= 1

        if guessed2 < generated:
            print(f"You need to go higher! ({lives} lives left)\n")
        elif guessed2 > generated:
            print(f"You need to go lower! ({lives} lives left)\n")
        else:
            print("\nCongratulations! You guessed the correct number!\n")
            points += 1
            break

    # If user didn't guess correctly in time
    if guessed2 != generated:
        print(f"You ran out of lives! The correct number was {generated}.")
        print("Points reset to 0!\n")
        points = 0

    print(f"You currently have {points} point{'s' if points != 1 else ''}.\n")

    again = input("Would you like to play again? (Y/N): ").strip().upper()
    if again == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Thanks for playing!")
        sys.exit()