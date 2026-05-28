#PARSA KOUCHEKI
#Rock Paper Scissors
#A simulation of the popular rock paper scissors game where the players play against the computer

#init
import random

#functions
win = 0
loss = 0
tie = 0

def rps():
    global win
    global loss
    global tie
    while True:
        player_choice = input("Welcome to RPS! Would you like to play Rock, Paper, or Scissors: ").lower()
        computer_choice = random.randint(1,3)
        if player_choice == "rock" and computer_choice == 1:
            print("You tied with the computer.")
            tie = tie + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "paper" and computer_choice == 2:
            print("You tied with the computer.")
            tie = tie + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "scissors" and computer_choice == 3:
            print("You tied with the computer.")
            tie = tie + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "rock" and computer_choice == 3:
            print("Computer played scissors. You win!")
            win = win + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "paper" and computer_choice == 1:
            print("Computer played rock. You win!")
            win = win + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "scissors" and computer_choice == 2:
            print("Computer played paper. You win!")
            win = win + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "rock" and computer_choice == 2:
            print("Computer played paper. You lose :(")
            loss = loss + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "paper" and computer_choice == 3:
            print("Computer played paper. You lose :(")
            loss = loss + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "scissors" and computer_choice == 1:
            print("Computer played rock. You lose :(")
            loss = loss + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "67234":
            god_mode()
        else:
            print("Please type Rock, Paper, or Scissors.")
            continue
def god_mode():
    global win
    global loss
    global tie
    print("God mode enabled")
    while True:
        player_choice = input("Welcome to RPS! Would you like to play Rock, Paper, or Scissors: ").lower()
        if player_choice == "rock":
            print("You win.")
            win = win + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "paper":
            print("You win.")
            win = win + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
        elif player_choice == "scissors":
            print("You win.")
            win = win + 1
            print(f"won = {win}")
            print(f"loss = {loss}")
            print(f"tie = {tie}")
            continue
#main
rps()
