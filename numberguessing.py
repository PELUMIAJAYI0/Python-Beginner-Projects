import random 

user_name = input("Input yout username---> ")
while True:
    highest_of_range = input("Input a number---> ")
    if highest_of_range.isdigit():
        highest_of_range = int(highest_of_range)

        if highest_of_range <= 0:
            print("Please tyoe a number greater than Zero(0) nest time")
            quit()
    else:
        print("...You didnt input a number, Please input a number next time...")
        quit()

    random_number = random.randint(0,highest_of_range)
    
    number_of_guesses = 0
    while True:
        number_of_guesses +=1
        user_guess = input("Make a guess---> ")
        if user_guess.isdigit():
            user_guess = int(user_guess)

            if user_guess <= 0:
                print("Please tyoe a number greater than Zero(0) nest time")
                quit()

        else:
            print("...You didnt input a number, Please input a number next time...")
            

        if user_guess == random_number:
            print(f"{user_name} guessed correctly, Congratulations!!!")
            print("You got it in", number_of_guesses, "guesses")
            print(f"The random number is---> {random_number}")

        elif user_guess > random_number:
                print("You guessed above the number")
        elif user_guess < random_number:
                print("You gessed below the number")
        else:
            print(f"{user_name} guessed wrongly, I am sorry!!!")
            print("You got it wrong", number_of_guesses, "guesses")
        
        cont = input("Do you want to continue? (yes/no)---> ")
        if cont == "no":
            quit()


        
        

        

