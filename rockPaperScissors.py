#allows for the user to play with a computer, computer's choice is randomised

import random

#point system
player_score = 0
computer_score = 0
history = []
def get_computer_choice():
    choices = "Rock","Paper", "Scissors"
    computer_choice = random.choice(choices)
    return computer_choice

def get_player_choice():
    print("""Welcome to Rock, Paper, Scissors! Here are the rules:

    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock If both choices are the same, it's a tie.""")

    while True:
        player_choice = input("Enter your choice: rock/paper/scissors ").lower()
        if player_choice == 'rock' or player_choice == 'scissors' or player_choice == 'paper':
            return player_choice
        else:
            print("Invalid choice. Please choose rock, paper or scissors")


def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        result = f"You chose : {player_choice} | Computer chose: {computer_choice}. It's a tie!"

    elif player_choice == "rock" and computer_choice == "scissors" or \
            player_choice == "paper" and computer_choice == "rock" or \
            player_choice == "scissors" and computer_choice == "paper":
        result = f"You chose: {player_choice} | Computer chose: {computer_choice}. You win!"
        player_score += 1
    else:
        result = f"You chose: {player_choice} | Computer chose: {computer_choice}. Computer wins!"
        computer_score += 1
    history.append(result)
    print(result)

def display_scores_and_history():
    print(f"\nScores:\nPlayer: {player_score}\nComputer: {computer_score}")
    print("\nMatch History:")
    for i, entry in enumerate(history, start=1):
        print(f"Match {i}: {entry}")

def main():
    global player_score, computer_score, history

    while True:

        action = input("Select an option: P - Play | S - See Score/History | Q - Quit").lower()

        if action == 'p':
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            determine_winner(player_choice, computer_choice)

        if action == 's':
            display_scores_and_history()

        elif action == 'q':
            print("Final Scores: ")
            display_scores_and_history()
            break

if __name__ == "__main__":
    main()

