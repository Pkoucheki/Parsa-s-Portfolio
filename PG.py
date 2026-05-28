#Parsa
#Pokemon Game
#INIT
import random
name = "gastly"
level = 0
day = 1
#Functions
def pictures():
    global name
    if name == "gastly":
        gastly()
    elif name == "haunter":
        haunter()
    elif name == "gengar":
        gengar()

def gastly():
    print((r"                            _\n"))
    print((r"                         .\"' `..._\n"))
    print((r"                        '         `.\n"))
    print((r"                      .'      ___..'\n"))
    print((r"                _   .\"       '   .__,-.,\"\", ,----.\n"))
    print((r"     ,.-\"\"''-..\" :  :        `--'        ' :      :\n"))
    print((r"   .'            :_,'                    `._`\"--. ;\n"))
    print((r"   :              _,.--'\"'\"\"`--._           `.  `\"\n"))
    print((r"  j             ,'               `-.      ,._.'  ,\"\".\n"))
    print((r"  :           ,'                   ,-.   .   __  `..'\n"))
    print((r"  `--.    .'.'                   ,'   `. :_,\"  `.\n"))
    print((r",.   ;   .   \\                 ,'      |         `.\n"))
    print(("' :  :    |    `.             ,'        |\\         `.  _\n"))
    print((r"`.   ._  |      \\         _.'          | .      ___ `\" :\n"))
    print((r"       : '     . \\      ,'  .          ' |     :   `...'\n"))
    print((r"      ,'  \\       `.   .             ,'  |     '  __\n"))
    print((r"     .    `.       |    \\          .'    '    .  (  `.\n"))
    print((r"   .'      \\`.___,'      `-.____.-'     '     :   `-.'\n"))
    print((r"    .   ,\". \\ ..___              _     /      :    .\n"))
    print((r"    :   . :  \\|/\\  `\"'--------+\"|,'  ,'       `-..' :\n"))
    print((r"     `-\" .'   `: `\"-.._______,.\\|  .'               '\n"))
    print((r"         `--. _ `._             _,'        ,\"\"-.__,'\n"))
    print((r"             \" :   `\"--.....--\"'     __   .\n"))
    print((r"             ,-'                 ,.-\"  `-'\n"))
    print((r"            :   ,..             .    ,\"\".\n"))
    print((r"           .'   .  :   __..._   `\"-. :   :\n"))
    print((r"           `.._  : ' ,'      `\"--..' `--\"\n"))
    print((r"               `-' `\" mh\n"))
def haunter():
    print((r"              -._                                   _.\n"))
    print((r"               \\ `-.._                           _,' |\n"))
    print((r"                \\     `-._    _,.--------.._  _.\"    '\n"))
    print((r"                 \\        `--'              ``.     /\n"))
    print((r"                  \\                                j    __\n"))
    print(("__         __       \\                               |.-\"' /\n"))
    print((r"`.`-.`-.__`.`'\"----\"\\                              |    /\n"))
    print((r"   `.       `.       '        ._                       /\n"))
    print((r"   `..        \\               | `.               /|   /\n"))
    print((r"     `.        `.             |   `._          .' |  /\n"))
    print((r"       `.  .-----`            |      `.       /   ' '\"\"''\n"))
    print((r"         `. `.            .    ._      `_    /  ,'    .'\n"))
    print((r"           `. `.           `._   `'\"\"'\"'     \"\"' ,  ,'\n"))
    print((r"             `. `.          `.`.              ,-/ ,'       _..\n"))
    print((r"               `. `.          \\|,---..  ,--\"./ / ,--------\".  \\\n"))
    print((r"                 `._           `.     `/ , .`.',:           \\  \\\n"))
    print((r"                    `._          `..\".,./ ' _.' :            \\  `.\n"))
    print((r"                  ,-'\" `-._              _.\"     .   |.-\"`.   \\  |\n"))
    print((r"                 .         `-..........-'        |   `..   \\   |_'\n"))
    print((r"                 |           `\".                 `.._   .  '  ,'\n"))
    print((r"                 |         |   |                     `\"'    .'\n"))
    print((r"                 |   /\\    |'  '\n"))
    print((r"                 '  /  \\   ||   .\n"))
    print((r"                '   \\  '   |'   ;\n"))
    print((r"                 \\  '  \\   `...'\n"))
    print((r"                  `\"\"   `,' mh\n"))
def gengar():
    print((r"                |`._         |\\\n"))
    print((r"                `   `.  .    | `.    |`.\n"))
    print((r"                 .    `.|`-. |   `-..'  \\           _,.-'\n"))
    print((r"                 '      `-. `.           \\ /|   _,-'   /\n"))
    print((r"             .--..'        `._`           ` |.-'      /\n"))
    print((r"              \\   |                                  /\n"))
    print((r"           ,..'   '                                 /\n"))
    print((r"           `.                                      /\n"))
    print((r"           _`.---                                 /\n"))
    print((r"       _,-'               `.                 ,-  /\"-._\n"))
    print((r"     ,\"                   | `.             ,'|   `    `.\n"))
    print((r"   .'                     |   `.         .'  |    .     `.\n"))
    print((r" ,'                       '   ()`.     ,'()  '    |       `.\n"))
    print(("'-.                    |`.  `.....-'    -----' _   |         .\n"))
    print((r"/ ,   ________..'     '  `-._              _.'/   |         :\n"))
    print((r"` '-\"\" _,.--\"'         \\   | `\"+--......-+' //   j `\"--.. , '\n"))
    print((r"   `.'\"    .'           `. |   |     |   / //    .       ` '\n"))
    print((r"     `.   /               `'   |    j   /,.'     '\n"))
    print((r"       \\ /                  `-.|_   |_.-'       /\\\n"))
    print((r"        /                        `\"\"          .'  \\\n"))
    print((r"       j                                           .\n"))
    print((r"       |                                 _,        |\n"))
    print((r"       |             ,^._            _.-\"          '\n"))
    print((r"       |          _.'    `'\"\"`----`\"'   `._       '\n"))
    print((r"       j__     _,'                         `-.'-.\"`\n"))
    print((r"         ',-.,' mh\n"))

def evolve():
    global name
    global level
    if level == 20:
        print("Your pokemon has evolved into haunter!")
        name = "haunter"
    elif level == 50:
        print("Your pokemon has evolved into gengar!")
        name = "gengar"
def question():
    global name
    global level
    global day
    while True:
        question = input(f"""today is day {day}. What do you want to do?:
train
rest
battle
boss battle
                         """)
        if question == "rest":
            print(f"Pokemon name: {name}")
            print(f"Your current level: {level}")
            pictures()
            day = day + 1
            continue
        elif question == "train":
            print("Your pokemon did 10 pushups!")
            level = level + 1
            day = day + 1
            evolve()
            continue
        elif question == "battle":
            number = random.randint(1,10)
            if number <= 3:
                print("You lost the battle")
                day = day + 1
                continue
            elif number > 3:
                level = level + 2
                print("You won the battle and got 2 levels!")
                evolve()
                day = day + 1
                continue
        elif question == "boss battle":
            if name == "gastly":
                number = random.randint(1,10)
                if number <= 1:
                    print("You won the battle!")
                    print("""
⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀
⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠃⠀⠀⠀⠀⠀⠀""")
                    break
                elif number > 1:
                    print("You lost the battle")
                    day = day + 1
                    continue
            elif name == "haunter":
                number = random.randint(1,10)
                if number <= 7:
                    print("You won the battle!")
                    print("""
⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀
⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀""")
                    break
                elif number > 3:
                    print("You lost the battle")
                    day = day + 1
                    continue
            elif name == "gengar":
                number = random.randint(1,10)
                if number <= 5:
                    print("You won the battle!")
                    print("""
⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀
⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀""")
                    break
                if number > 5:
                    print("You lost the battle")
                    day = day + 1
                    continue

        elif level == 50:
            break
#main

question()
