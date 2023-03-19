from subprocess import call

def menu():
    print("Welcome to the AI Trainer Workout")
    print("---------------------------------")
    print("\n")
    print("What would you like to workout today?")
    print("1. Bicep Curls")
    print("2. Dumbbell Shoulder Press")
    print("3. Jumping Jacks")
    print("4. Quit")
    print("\n")

    choice = input("Please pick one: ")
    return choice

choice = menu()


def open_bicep_curl():
    call(["python", "bicep_curl.py"])

def open_shoulder_press():
    call(["python", "shoulder_press.py"])

def open_jumping_jacks():
    call(["python", "jumping_jacks.py"])

while choice != "4":
    if choice == "1":
        open_bicep_curl()
    elif choice == "2":
        open_shoulder_press()
    elif choice == "3":
        open_jumping_jacks()
    elif choice == "4":
        break
    else:
        print("Not valid choice")
        choice = input("Please pick again: ")
    
