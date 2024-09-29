print("...Welcome to the Quiz game...")

play = input("Do you want to play the quiz game---> ")
while True:
    
    if play in ["no", "No"]:
        print("...Esixting Quiz Game...")
        quit()
    else:
        print("Okay let's play and have fun :)")
        score = 0 #to keep track of the correct answer

        answer = input("What does CPU stand for---> ")
        if answer == "Central Processing Unit":
            print("You got it correctly")
            score +=1
        else: 
            print("You got it wrong")

        answer = input("What does GPU stand for---> ")
        if answer == "Graphics Processing Unit":
            print("You got it correctly")
            score +=1
        else: 
            print("You got it wrong")

        answer = input("What does RAM stand for---> ")
        if answer == "Random Access Memory":
            print("You got it correctly")
            score +=1
        else: 
            print("You got it wrong")

        answer = input("What does ROM stand for---> ")
        if answer == "Read Only Memory":
            print("You got it correctly")
            score +=1
        else: 
            print("You got it wrong")

    print("You got " + str(score) + " questions correctly!!!")
    print("You got " + str((score/4)*100) + " %.")

    cont = input("Do you want you continue playing(yes/no)---> ")
    if cont.lower == "no":
        quit()
    

