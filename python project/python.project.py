
"""
Created on Mon Apr  1 10:38:54 2024

@author: akshd
"""
value = input("Choose (1) for rock paper scissors, (2) for haunted mension little story advanture, (3) black jack game, (Virtual Casino) ")

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    you = None
    computer = random.choice(options)

    while you not in options:
        you = input("rock(✊), paper(🤚), scissors(✌) ? ")

    print(f"you: {you}")
    print(f"Computer: {computer}")

    if you == computer:
        print("It's a tie!")
    elif you == "rock" and computer == "scissors":
        print("rock(✊) win!")
    elif you == "paper" and computer == "rock":
        print("paper(🤚) win!")
    elif you == "scissors" and computer == "paper":
        print("scissors(✌) win!")
    else:
        print("You lose! (☹️)")

    play_again = input("Play again? (y/n): ")
    if play_again == 'n':
            running = False

print("That was fun to play!")