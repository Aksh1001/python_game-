import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def calculate_sum(dice):
    return sum(dice)

def print_dice_faces(dice):
    dice_faces = [
        """
        -------
        |     |
        |  o  |
        |     |
        -------""",
        """
        -------
        | o   |
        |     |
        |   o |
        -------""",
        """
        -------
        | o   |
        |  o  |
        |   o |
        -------""",
        """
        -------
        | o o |
        |     |
        | o o |
        -------""",
        """
        -------
        | o o |
        |  o  |
        | o o |
        -------""",
        """
        -------
        | o o |
        | o o |
        | o o |
        -------"""
    ]

    print("Dice:")
    for i in range(2):
        print(dice_faces[dice[i] - 1])

def gambling_game():
    print("Welcome to the Gambling Casino Dice Game!")

    balance = 100  # starting balance
    while balance > 0:
        print("\nYour balance:", balance)

        guess = int(input("Guess the number on the dice (1-6): "))
        if guess < 1 or guess > 6:
            print("Invalid guess. Please enter a number between 1 and 6.")
            continue

        bet = int(input("Place your bet (minimum bet is 1): "))
        if bet < 1 or bet > balance:
            print("Invalid bet amount. Please place a valid bet.")
            continue

        print("Rolling the dice...")
        player_dice = roll_dice()
        print_dice_faces(player_dice)
        player_sum = calculate_sum(player_dice)

        if guess in player_dice:
            print(f"Congratulations! The number {guess} appeared on the dice! You win double your bet!")
            balance += bet * 2
        else:
            print(f"Sorry, the number {guess} did not appear on the dice. You lost your bet.")
            balance -= bet

        if balance <= 0:
            print("Sorry, you're out of money. Game over!")
            break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    gambling_game()
