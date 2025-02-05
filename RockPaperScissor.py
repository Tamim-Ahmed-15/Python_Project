import random

# Options for the game
choices = ["rock", "paper", "scissors"]

# Score tracking
player_wins = 0
computer_wins = 0
draws = 0

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' to stop playing.\n")

play=input("Do you want to play? (yes/no) : ")
if play!='yes':
    print("Maybe next time! Goodbye!")
else:
    while True:
        # Player's choice
        player_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()

        # Option to exit the game
        if player_choice == "exit":
            break

        # Validate input
        if player_choice not in choices:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.\n")
            continue

        # Computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a draw!\n")
            draws += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            print("You win! 🎉\n")
            player_wins += 1
        else:
            print("Computer wins! 😢\n")
            computer_wins += 1

    # Final results
    print("\nGame Over! Here are your final results:")
    print(f"🏆 You won: {player_wins} times")
    print(f"🤖 Computer won: {computer_wins} times")
    print(f"⚖️ Draws: {draws}")
    print("Thanks for playing! 🎮")



