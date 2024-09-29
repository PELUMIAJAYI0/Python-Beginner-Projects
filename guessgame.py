from  random import randint 
print("...Welcome to The Guess Game..")

rad = randint(1,10)
username = input("Input your name---> ")
timesOfPlay = int(input("Input thr number of times you want to play---> "))
count = 0
while count < timesOfPlay:
    you = randint(1,2)
    guess = int(input("Input the number you guess(ed)---> "))
    if guess == you:
        print(F"{username} wins, Congratulations!!!")
    else:
        print("Wronged guess, you can try again!!!")
        count +=1

cont = input("Do you want to continue? (yes/no)---> ")
if cont in ["no", "yes"]:
    quit()
