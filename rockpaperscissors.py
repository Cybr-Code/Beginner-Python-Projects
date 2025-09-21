import random
import os
import sys

# Intro
print("Rock, Paper, Scissors!\n")
print("You have to beat the computer in a game of Rock, Paper, Scissors!\n")

choices = ["Rock", "Paper", "Scissors"]
rules = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

while True:
    computer_choice = random.choice(choices)

    # Ask user for input
    while True:
        human_choice = input("Rock, Paper, or Scissors?: ").strip().capitalize()
        if human_choice in choices:
            break
        else:
            print("Please enter Rock, Paper, or Scissors!\n")

    # Decide outcome
    if human_choice == computer_choice:
        status = "tied"
    elif rules[human_choice] == computer_choice:
        status = "won"
    else:
        status = "lost"

    # Print result
    if status == "tied":
        print(f"You tied! You both chose {human_choice}.\n")
    else:
        print(f"You {status}! You chose {human_choice}, computer chose {computer_choice}.\n")

    again = input("Would you want to play again? Y/N: ").strip().upper()
    if again == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif again == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Exiting.")
        break
