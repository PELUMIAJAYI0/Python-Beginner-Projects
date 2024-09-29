print("...Welcome to this roller coaster ride...")
user_name = input("Please, enter your name---> ")
user_age = int(input(f"{user_name}, please enter your age---> "))

if user_age >= 18 and user_age <= 45:
    print(f"...{user_name}, enjoy your side...")
elif user_age < 18:
    print(f"{user_name}, you are too young for this ride, sorry :(")
else:
    print(f"{user_name}, you are too old for this ride, sorry :(")