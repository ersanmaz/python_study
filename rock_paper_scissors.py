import random

computer_choice = random.choice(["rock", "paper", "scissors"])

player_choice = input("rock, paper, or scissors? ").lower()

print("The computer chose", computer_choice)

if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")