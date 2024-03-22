# Create a game of rock paper scissors on the terminal:
# The game should randomly select rock, paper, or scissors
# The game should prompt the user to select rock, paper, or scissors
# The game should compare the user's selection to the game's selection
# The game should display the winner
# The game should ask the user if they want to continue playing
# The game should inform the player if the option entered is invalid
# When the user chooses to not continue, the game should display the user's final number of wins and losses

import random

def rock_paper_scissors():
    user_wins = 0
    user_losses = 0
    user_ties = 0
    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print(f"Computer chose {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie!")
                user_ties += 1
            elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
                print("You win!")
                user_wins += 1
            else:
                print("You lose!")
                user_losses += 1
        else:
            print("Invalid choice")
        continue_playing = input("Do you want to continue playing? (yes/no): ")
        if continue_playing == "no":
            print(f"User wins: {user_wins}")
            print(f"User losses: {user_losses}")
            print(f"User ties: {user_ties}")
            break

rock_paper_scissors()