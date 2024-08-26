#random number guess game
import random

print("...Welcome to the Number Guess Game...") #prints welcome message
name = input("Enter your name---> ") # prompts user to input their name and stores it in a varaiable called name
number = int(input("Type the highest number you want to gess up to---> ")) #prompts the user to enter the highest number they want to guess up to
secret = random.randint(1, number) #generates a random integer number between 1 and {number}
guess = 0 #intialize a guess

while guess != secret:
    guess +=1 #incrementes guess variable by 1
    guess = int(input(f"Guess a number between 1 and {number}---> "))#prompts user to enter a guess
    if guess<secret:
        print(f"{name} please guess higher")
    elif guess > secret:
        print(f"{name} plase guess lower")
    else:
        print(f"{name} You have won, congratulations!!!")