#Parsa
#Create the To-do List App that allows the user to keep track of items that must get done during the day.

#Init

#Functions
def todo():
    list = []
    Done = []
    while True:
        start = input("Welcome to the to-do app! Would you like to do to your list (add, done, remove, clear, or leave)?: ").lower()
        if start == "add":
            add = input("What would you like to add to the list?: ").strip()
            if add == "":
                print("Please enter a real task")
                continue
            list.append(add)
            print(f"Your current things to do: {list}")
            print(f"Things you have completed: {Done}")
            continue
        elif start == "done":
            try:
                remove = int(input("What is the number assigned to the task you completed (task1 = 0, task5 = 4)?: "))
            except:
                print("Please say the correct number that is assigned to the task")
                continue
            if remove > (len(list) - 1) or remove < 0:
                print("Please say the correct number that is assigned to the task")
                continue
            complete = list[remove]
            Done.append(complete)
            list.pop(int(remove))
            print(f"Your current things to do: {list}")
            print(f"Things you have completed: {Done}")
            continue
        elif start == "remove":
            try:
                remove = int(input("What is the number assigned to the task you completed (task1 = 0, task5 = 4)?: "))
            except:
                print("Please say the correct number that is assigned to the task")
                continue
            if remove > (len(list) - 1) or remove < 0:
                print("Please say the correct number that is assigned to the task")
                continue
            list.pop(int(remove))
            print(f"Your current things to do: {list}")
            print(f"Things you have completed: {Done}")
            continue
        elif start == "clear":
            list.clear()
            print("You have cleared your list")
            print(f"Your current things to do: {list}")
            print(f"Things you have completed: {Done}")
            continue
        elif start == "leave":
            print("Bye! Thanks for using To-do.")
            break
        else:
            print("Please pick either add, done, remove, clear, or leave")
            continue


#main
todo()

