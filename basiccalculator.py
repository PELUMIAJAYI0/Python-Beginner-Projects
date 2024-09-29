import math 

def add(a, b):
    answer = a+b
    #print(str(a)+ "+" +  str(b)+ "=" + str(answer))
    print(f"The Addition of both numbers is--->",answer)

def sub(a, b):
    answer = a - b
    #print(str(a)+ "-" +  str(b)+ "=" + str(answer))
    print(f"The Subtraction of both numbers is--->",answer)

def mul(a, b):
    answer = a * b
    #print(str(a)+ "*" +  str(b)+ "=" + str(answer))
    print(f"The Multiplication of both numbers is--->",answer)

def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed, It is a Math error")
    else:
        answer = a / b
        #print(str(a)+ "/" +  str(b)+ "=" + str(answer))
    print(f"The Division of both numbers is--->",answer)

def sqr(a):
    answer = a ** 2
    #print(str(a)+ "^2" + "=" + str(answer))
    print(f"The Square of the number is--->",answer)

def sqr(b):
    answer = b ** 2
    #print(str(b)+ "^2" + "=" + str(answer))
    print(f"The Square of the number is--->",answer)

def sqrt(a):
    """if answer.is_integer():
        return int(answer)
    else:
        print("...The Number Inputted is not a perfect integer number...")"""

    answer = math.sqrt(a)
    print(f"The square root of the number is---> ", answer)

def sqrt(b):
    answer = math.sqrt(b)
    print(f"The square root of the number is---> ", answer)


#to keep looping until the user says stop
while True: 
    print("A---> Addition")
    print("B---> Subtraction")
    print("C---> Multiplication")
    print("D---> Division")
    print("E---> Square")
    print("F---> SquareRoot")
    print("G---> Exist")

    options = input("Input any options from above to perform calculation on---> ")

    if options == "a" or options =="A":

        print("Addition")
        a = int(input("Input your first number---> "))
        b = int(input("Input your second number---> "))
        add(a, b)

    elif options == "b" or options =="B":
        print("Subtraction")
        a = int(input("Input your first number---> "))
        b = int(input("Inpt your second number---> "))
        sub(a, b)

    elif options == "c" or options =="C":
        print("Multiplication")
        a = int(input("Input your first number---> "))
        b = int(input("Input your second number---> "))
        mul(a, b)

    elif options == "d" or options =="D":
        print("Division")
        a = int(input("Input your first number---> "))
        b = int(input("Input your second number---> "))
        div(a, b)

    elif options == "e" or options == "E":
        print("Square")
        a = int(input("Input your number---> "))
        sqr(a)
        b = int(input("Input your number---> "))
        sqr(b)
    
    elif options == "f" or options == "F":
        print("SquareRoot")
        a = int(input("Input a perfect number---> "))
        sqrt(a)
        b = int(input("Input a perfect number---> "))
        sqrt(b)
    
    elif options == "g" or options == "G":
        print("Exiting the Calculator, Goodbye!!!")
    
    cont = input("Do you want to continue? (yes/no)---> ")
    if cont.lower() == "no":
        quit()
