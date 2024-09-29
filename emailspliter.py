#a program that take an email address and breaks it down into the user and the domain
#collect email from user
#split the email using the @, save te=he first part as the username, the second part as the domain
#splict domain using .com or any other 

def main():
    print("...Welcome to the Email Spliter...")
    print("")

    email_input = input("Input your email address---> ")
    #split the email using the @
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("The Username of the email address is---> ", username)
    print("The Domain of the email address is---> ", domain)
    print("The Extension of the email address is---> ", extension)

while True:
    main()
    cont = input("\n Do you want to continue? (yes/no)---> ")
    if cont.lower() == "no":
        quit()
    



