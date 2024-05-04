import random

def rock_paper_scissors():
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
            break

    print("That was fun to play!")


def haunted_mansion():
    import time
    import random

    print("Welcome to the Haunted Mansion!")
    print("You are a distant family member of a rich millionaire who has just passed away, leaving this mansion to you.")
    print("As the newfound owner, you decide to pay a visit to the mansion.")
    print("The house is dated, creaky, and falling apart. You walk in the front door, the eerie silence engulfing you.")
    print("Do you want to enter the living room, the dining room, or explore the upstairs?")

    roomChoice = input("> ")

    if roomChoice == "living room":
        print("You enter the living room.")
        print("As you walk in, a cold draft sends shivers down your spine. The room feels oppressively dark, despite the dim light filtering in through the dusty windows.")
        print("Your eyes are drawn to a glint of gold on a nearby table, illuminated by the faint light. You approach cautiously.")
        print("Do you want to steal the jewelry from the table or leave it alone?")

        pitBullChoice = input("> ")

        if pitBullChoice == "steal":
            print("You reach for the jewelry, but as your fingers brush against it, a low growl fills the room.")
            print("You freeze, feeling an icy breath on the back of your neck. The shadows seem to come alive, swirling around you menacingly.")
            print("Suddenly, the room is plunged into darkness, and you hear the snarls of an unseen beast.")
            print("In a panic, you fumble for the door, desperate to escape the malevolent presence.")
            print("You burst out of the room, heart pounding, but the feeling of dread lingers.")
        elif pitBullChoice == "leave":
            print("You decide to heed the warning signs and leave the jewelry untouched, fearing what dark forces may be guarding it.")
            print("You hurriedly exit the living room, relieved to be away from its oppressive atmosphere.")
        else:
            print("Invalid choice. Please try again.")

    elif roomChoice == "dining room":
        print("You chose to go into the dining room.")
        print("As you step into the dining room, the air grows thick with a musty smell, and the temperature drops unnervingly.")
        print("Your gaze is drawn to a grand dining table covered in a tattered cloth. On it sits a lone candle, flickering ominously.")
        print("Do you want to approach the candle, explore further, or leave the room?")

        diningChoice = input("> ")

        if diningChoice == "approach candle":
            print("You cautiously approach the candle, its flame casting dancing shadows across the room.")
            print("As you reach out to touch it, a ghostly figure materializes before you, its eyes hollow and full of malice.")
            print("You feel a cold hand wrap around your wrist, freezing you in place as the figure whispers dark incantations.")
            print("In a burst of terror, you wrench yourself free and flee from the room, the echoes of sinister laughter following you.")
        elif diningChoice == "explore further":
            print("You decide to explore the room further, searching for any clues or items of interest.")
            print("As you move deeper into the room, the shadows seem to elongate and twist, taking on sinister forms.")
            print("Suddenly, the walls begin to close in, trapping you in a suffocating embrace.")
            print("With a surge of adrenaline, you push against the walls and manage to escape, gasping for breath.")
        elif diningChoice == "leave":
            print("You decide to trust your instincts and leave the room, unwilling to risk encountering whatever malevolent presence lurks within.")
            print("As you exit the dining room, you can't shake the feeling of being watched.")
        else:
            print("Invalid choice. Please try again.")

    elif roomChoice == "explore upstairs":
        print("You climb the creaky staircase to the second floor, the steps groaning ominously with each footfall.")
        print("As you reach the top, the air grows colder, and a sense of dread settles over you like a heavy shroud.")
        print("Two doors stand before you, their ancient wood warped and weathered.")
        print("Do you want to enter the left room, the right room, or go back downstairs?")

        upstairsChoice = input("> ")

        if upstairsChoice == "left room":
            print("You cautiously open the door to the left room, the hinges squealing in protest.")
            print("The room is cloaked in darkness, the only illumination coming from a single, flickering candle on an old wooden dresser.")
            print("As you step inside, the door slams shut behind you with a deafening thud, sealing you in darkness.")
            print("Panic rising, you frantically search for a way out, but the room seems to shift and warp, disorienting you.")
            print("Just as you fear you'll be trapped forever, the door creaks open, and you stumble out into the hallway, breathless and shaken.")
        elif upstairsChoice == "right room":
            print("You enter the right room, the air heavy with the scent of decay and mildew.")
            print("The room is dominated by a towering wardrobe, its doors slightly ajar, revealing darkness within.")
            print("As you approach, a chill runs down your spine, and you sense a presence lurking within.")
            print("Do you want to open the wardrobe or leave the room?")

            wardrobeChoice = input("> ")

            if wardrobeChoice == "open wardrobe":
                print("You summon your courage and pull open the wardrobe doors, revealing nothing but darkness.")
                print("Suddenly, skeletal hands shoot out from the shadows, grasping at you with bony fingers.")
                print("With a scream, you recoil, stumbling backwards and fleeing from the room in terror.")
            elif wardrobeChoice == "leave":
                print("You decide to trust your instincts and leave the room, unwilling to tempt fate any further.")
                print("As you exit the room, you can't shake the feeling of eyes boring into your back.")
            else:
                print("Invalid choice. Please try again.")
        elif upstairsChoice == "go back downstairs":
            print("You decide to retreat downstairs, the oppressive atmosphere of the second floor weighing heavily on you.")
            print("As you descend the staircase, a sense of relief washes over you, but the feeling of unease lingers.")
        else:
            print("Invalid choice. Please try again.")

    else:
        print("Invalid choice. Please try again.")



def gambling_game():
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


def main():
    while True:
        print("\nMenu:")
        print("1. Rock Paper Scissors")
        print("2. Haunted Mansion")
        print("3. Gambling Game")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            haunted_mansion()
        elif choice == '3':
            gambling_game()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()

