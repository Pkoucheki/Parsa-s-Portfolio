#CREATE project

import pandas as pd
import random

data1 = pd.read_csv("validWordleGuess.csv")
data2 = pd.read_csv("validWordleAnswers.csv")

validWordleGuess = data1['validWordleGuess'].tolist()
validWordleAnswer = data2['validWordleAnswer'].tolist()
guesses = []
answer = []

attempts = 1

def Wordle(guess, Answer):
    guesses.clear()
    splitguess = list(guess)
    guesses.append(splitguess)
    global attempts
    for i in range(len(guesses)):
            for j in range(len(guesses[i])):
                if guesses[i][j] in Answer and guesses[i][j] == Answer[j]:
                    print(f"{guesses[i][j]} is in the word and in the correct spot. 🟢")
                elif guesses[i][j] in Answer and guesses[i][j] != Answer[j]:
                    print(f"{guesses[i][j]} is in the word but in the wrong spot. 🟡")
                elif guesses[i][j] not in Answer:
                    print(f"{guesses[i][j]} is not in the word in any spot. 🔴")
    attempts = attempts + 1

def GAME():
    answer.clear()
    while True:
        welcome = input("Welcome to Wordle. Type play, exit, or HTP (how to play): ").lower()
        if welcome == "play":
            won = False
            randomnumber = random.randint(0,2307)
            Answer = validWordleAnswer[randomnumber]
            splitanswer = list(Answer)
            answer.append(splitanswer)
            while True:
                guess1 = input("Enter your first guess. You have 5 guesses left: ").lower()
                if len(guess1) != 5:
                    print("The word must be 5 letters")
                    guesses.clear()
                    continue
                if guess1 not in validWordleAnswer:
                    print("Please input a valid word")
                    guesses.clear()
                    continue
                Wordle(guess1, Answer)
                if guess1 == Answer:
                    print("You guessed the word!")
                    won = True
                    break
                guesses.clear()
                break
            if won:
                pass
            while True:
                if won:
                    break
                guess2 = input("Enter your second guess. You have 4 guesses left: ").lower()
                if guess2 == guess1:
                    print("You already guessed this word. Retry your second guess.")
                    guesses.clear()
                    continue
                if len(guess2) != 5:
                    print("The word must be 5 letters")
                    guesses.clear()
                    continue
                if guess2 not in validWordleAnswer:
                    print("Please input a valid word")
                    guesses.clear()
                    continue
                Wordle(guess2, Answer)
                if guess2 == Answer:
                    print("You guessed the word!")
                    won = True
                    break
                guesses.clear()
                break
            if won:
                pass
            while True:
                if won:
                    break
                guess3 = input("Enter your third guess. You have 3 guesses left: ").lower()
                if guess3 == guess2 or guess3 == guess1:
                    print("You already guessed this word. Retry your third guess.")
                    guesses.clear()
                    continue
                if len(guess3) != 5:
                    print("The word must be 5 letters")
                    guesses.clear()
                    continue
                if guess3 not in validWordleAnswer:
                    print("Please input a valid word")
                    guesses.clear()
                    continue
                Wordle(guess3, Answer)
                if guess3 == Answer:
                    print("You guessed the word!")
                    won = True
                    break
                guesses.clear()
                break
            if won:
                pass
            while True:
                if won:
                    break
                guess4 = input("Enter your fourth guess. You have 2 guesses left: ").lower()
                if guess4 == guess3 or guess4 == guess2 or guess4 == guess1:
                    print("You already guessed this word. Retry your fourth guess.")
                    guesses.clear()
                    continue
                if len(guess4) != 5:
                    print("The word must be 5 letters")
                    guesses.clear()
                    continue
                if guess4 not in validWordleAnswer:
                    print("Please input a valid word")
                    guesses.clear()
                    continue
                Wordle(guess4, Answer)
                if guess4 == Answer:
                    print("You guessed the word!")
                    won = True
                    break
                guesses.clear()
                break
            if won:
                pass
            while True:
                if won:
                    break
                guess5 = input("Enter your last guess: ").lower()
                if guess5 == guess4 or guess5 == guess3 or guess5 == guess2 or guess5 == guess1:
                    print("You already guessed this word. Retry your last guess.")
                    guesses.clear()
                    continue
                if len(guess5) != 5:
                    print("The word must be 5 letters")
                    guesses.clear()
                    continue
                if guess5 not in validWordleAnswer:
                    print("Please input a valid word")
                    guesses.clear()
                    continue
                Wordle(guess5, Answer)
                if guess5 == Answer:
                    print("You guessed the word!")
                    won = True
                    continue
                else:
                    print(f"Sorry, you're out of guesses! The word was: {Answer} 🔴")
                guesses.clear()
                break
        elif welcome == "exit":
            print("Thank you for playing")
            break
        elif welcome == "htp":
            print("""
How To Play:
Guess the Wordle in 5 tries.
Each guess must be a valid 5-letter word.
The color next to the letter will change to show how close your guess was to the word.
🟢 is in the word and in the correct spot.
🟡 is in the word but in the wrong spot.
🔴 is not in the word in any spot.
""")
            continue
        else:
            print("Either Play or Exit.")
            continue
GAME()

#sources
#https://www.nytimes.com/games/wordle/index.html
#10,000 valid Wordle guesses and answers from the NYT
