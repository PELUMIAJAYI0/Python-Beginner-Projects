import random

def get_choices():
    player_choice = input("Input yout choice (rock, paper scissors)---> ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print("You chose---> "+ player +", Computer chose---> " + computer)
    if player == computer:
        print("It's a tie") 

    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! YOu win")
        else:
            print("Paper covers rock! YOu lose")
            
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! YOu win")
        else:
            print("Scissors cut paper! YOu lose")
    
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cut paper! YOu win")
        else:
            print("Rock smashes scissors! YOu lose")
    

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)