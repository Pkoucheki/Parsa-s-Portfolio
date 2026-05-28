#Parsa
#Slot machine
#Init
import random
points = 0
#functions
def machine():
    global points
    while True:
        play = input("""Welcome to Slot Machine! 10 credits to play. Type (y/N) to play
Type credits to view credits
Type add to add credits: """).lower()
        if play == "y":
            symbols = ["🂡","🂡", "🂡","🂡", "⚅","⚅", "⚅","⚅", "⚡","⚡", "⚡","⚡", "7", "☆"]
            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            if slot1 == "🂡" and slot2 == "🂡" and slot3 == "🂡":
                print("""you rolled: 🂡 🂡 🂡
    small win of 75""")
                points = points + 75
                points = points - 10
                continue
            elif slot1 == "⚅" and slot2 == "⚅" and slot3 == "⚅":
                print("""you rolled: ⚅ ⚅ ⚅
    small win of 75""")
                points = points + 75
                points = points - 10
                continue
            elif slot1 == "⚡" and slot2 == "⚡" and slot3 == "⚡":
                print("""you rolled: ⚡ ⚡ ⚡
    small win of 75""")
                points = points + 75
                points = points - 10
                continue
            elif slot1 == "7" and slot2 == "7" and slot3 == "7":
                print("""💸💸💸 JACKPOT 💸💸💸
    you rolled: 7 7 7
    💸💸💸 350 CREDITS 💸💸💸""")
                points = points + 350
                points = points - 10
                continue
            elif points <= 0:
                print("You are out of credits. Please add more money.")
                continue
            elif slot1 == "☆" or slot2 == "☆" or slot3 == "☆":
                print("You got a wildcard. You get another spin.")
                print(f"{slot1} {slot2} {slot3}")
                wild = ["🂡","🂡", "🂡","🂡", "⚅","⚅", "⚅","⚅", "⚡","⚡", "⚡","⚡", "7"]
                wild1 = random.choice(wild)
                wild2 = random.choice(wild)
                if wild1 == "🂡" and wild2 == "🂡":
                    print("""you rolled: 🂡 🂡 ☆
    small win of 20""")
                    points = points + 20
                    points = points - 10
                    continue
                elif wild1 == "⚅" and wild2 == "⚅":
                    print("""you rolled: ⚅ ⚅ ☆
    small win of 20""")
                    points = points + 20
                    points = points - 10
                    continue
                elif wild1 == "⚡" and wild2 == "⚡":
                    print("""you rolled: ⚡ ⚡ ☆
    small win of 20""")
                    points = points + 20
                    points = points - 10
                    continue
                elif wild1 == "7" and wild2 == "7":
                    print("""you rolled: 7 7 ☆
    win of 200""")
                    points = points + 200
                    points = points - 10
                    continue
                else:
                    print("you lost wildcard")
                    print(f"{wild1} {wild2} ☆")
            else:
                print("You lost")
                print(f"{slot1} {slot2} {slot3}")
                points = points - 10
                continue
        elif play == "credits":
            print(f"credits = {points}")
            continue
        elif play == "n":
            print("Thanks for playing")
            print(f"You won {points} credits!")
            break
        elif play == "add":
            add = int(input("How many credits would you like to add (20, 50, 100): "))
            points = points + add
            if add != 20 or add != 50 or add != 100:
                print("You can only add 20, 50, or 100")
            continue
        if play == "1000":
            for i in range(1000):
                symbols = ["🂡", "⚅", "⚡", "7"]
                slot1 = random.choice(symbols)
                slot2 = random.choice(symbols)
                slot3 = random.choice(symbols)
                if slot1 == "🂡" and slot2 == "🂡" and slot3 == "🂡":
                    print("""you rolled: 🂡 🂡 🂡
        small win of 75""")
                    points = points + 75
                    points = points - 10
                    continue
                elif slot1 == "⚅" and slot2 == "⚅" and slot3 == "⚅":
                    print("""you rolled: ⚅ ⚅ ⚅
        small win of 75""")
                    points = points + 75
                    points = points - 10
                    continue
                elif slot1 == "⚡" and slot2 == "⚡" and slot3 == "⚡":
                    print("""you rolled: ⚡ ⚡ ⚡
        small win of 75""")
                    points = points + 75
                    points = points - 10
                    continue
                elif slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("""💸💸💸 JACKPOT 💸💸💸
        you rolled: 7 7 7
        💸💸💸 350 CREDITS 💸💸💸""")
                    points = points + 350
                    points = points - 10
                    continue
                elif slot1 == "☆" or slot2 == "☆" or slot3 == "☆":
                    print("You got a wildcard. You get another spin.")
                    print(f"{slot1} {slot2} {slot3}")
                    wild = ["🂡","🂡", "🂡","🂡", "⚅","⚅", "⚅","⚅", "⚡","⚡", "⚡","⚡", "7"]
                    wild1 = random.choice(wild)
                    wild2 = random.choice(wild)
                    if wild1 == "🂡" and wild2 == "🂡":
                        print("""you rolled: 🂡 🂡 ☆
        small win of 50""")
                        points = points + 20
                        points = points - 10
                        continue
                    elif wild1 == "⚅" and wild2 == "⚅":
                        print("""you rolled: ⚅ ⚅ ☆
        small win of 50""")
                        points = points + 20
                        points = points - 10
                        continue
                    elif wild1 == "⚡" and wild2 == "⚡":
                        print("""you rolled: ⚡ ⚡ ☆
        small win of 50""")
                        points = points + 20
                        points = points - 10
                        continue
                    elif wild1 == "7" and wild2 == "7":
                        print("""you rolled: 7 7 ☆
        small win of 275""")
                        points = points + 200
                        points = points - 10
                        continue
                    else:
                        print("you lost wildcard")
                        print(f"{wild1} {wild2} ☆")
                else:
                    points = points - 10
                    continue
            print(f"casino net profit: {1000 - points}")
        else:
            print("Select either y, n, cedits, or add.")
            continue




#main
machine()
