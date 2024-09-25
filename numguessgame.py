import random
attempt = 0
#attempt_times = int(input(f"{name}, how many times do you want to attempt the name---> "))

while True:
    print("...Welcome to Number Guess Game...")

    name = input("Enter your name---> ")
    print(f"{name}, you are highly welcome")


    upper = int(input(f"{name} enter the higest range of number you want to guess to---> "))
    lower = int(input(f"{name} enter the lowest range of number you want to guess to---> "))

    random_number = random.randint(lower, upper)

    user_num = int(input(f"{name} enter any number from {lower} to {upper}---> "))
    attempt += 1
    if user_num == random_number:
        print(f"{name}, congratulations you guessed {attempt} times :) ")
    else:
        print(f"{name}, sorry you guess wrongly :( ")


    cont = input(f"{name}, do you want to continue the Number Guessing Game (yes/no)---> ").lower()
    if cont != "no":
        continue
    else:
        print(f"{name}, is exiting the game, have a good day :) ")
        break

