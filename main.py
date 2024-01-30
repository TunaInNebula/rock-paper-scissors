import random

rock = "1"
paper = "2"
scissors = "3"
item_list = [rock, paper, scissors]

user_score = 0
cpu_score = 0

user_choice = ""
cpu_choice = ""

print("welcome to the game")
username = input("username: ")
print(f"{username}: {user_score}")
print(f"Rival: {cpu_score}")
print(f"-> 1. rock \n-> 2. paper \n-> 3. scissors")


def user_choose():
    global user_choice
    if int(user_choice) == 1:
        print("your choice is rock")
    elif int(user_choice) == 2:
        print("your chopice is paper")
    elif int(user_choice) == 3:
        print("your choice is scissors")
    else:
        print("Geçersiz Seçim!")


def cpu_choose():
    global cpu_choice
    cpu_choice = int(random.choice(item_list))
    if cpu_choice == 1:
        print("rival choosed rock")
    elif cpu_choice == 2:
        print("rival choosed paper")
    else:
        print("rival choosed scissors")


def game_start():
    global cpu_score
    global user_score

    if int(user_choice) == 1:
        if int(user_choice) == int(cpu_choice):
            print("draw")
        elif cpu_choice == 2:
            print("Rival +1")
            cpu_score += 1
        elif cpu_choice == 3:
            print(f"{username} +1")
            user_score += 1
    elif int(user_choice) == 2:
        if int(user_choice) == int(cpu_choice):
            print("draw")
        elif cpu_choice == 1:
            print(f"{username} +1")
            user_score += 1
        elif cpu_choice == 3:
            print("Rival +1")
            cpu_score += 1
    else:
        if int(user_choice) == int(cpu_choice):
            print("draw")
        elif cpu_choice == 1:
            print("Rival +1")
            cpu_score += 1
        elif cpu_choice == 2:
            print(f"{username} +1")
            user_score += 1


while True:
    print(f"{username}: {user_score}")
    print(f"Rival: {cpu_score}")
    if user_score < 3 and cpu_score < 3:
        user_choice = input("Make your choice: ")
        if 0 < int(user_choice) < 4:
            user_choose()
            cpu_choose()
            game_start()
        else:
            print("invalid selection!")
    elif user_score == 3:
        print(f"{username}: {user_score}")
        print(f"Rival: {cpu_score}")
        print(f"{username} WINS !")
        break
    elif cpu_score == 3:
        print(f"{username}: {user_score}")
        print(f"Rival: {cpu_score}")
        print("Rival WINS !!!")
        break

