"""Play one round of Rock, Paper, Scissors against the computer."""

import random


def main():
    choices = ("rock", "paper", "scissors")

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in choices:
            break
        print("Invalid choice. Please enter rock, paper, or scissors.")

    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Each key beats its corresponding value.
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if user_choice == computer_choice:
        print("It's a tie!")
    elif beats[user_choice] == computer_choice:
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()
