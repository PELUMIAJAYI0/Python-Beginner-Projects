def add(numbers):
    answer = sum(numbers)
    print(f"The Addition of the numbers is---> {answer}")

def sub(numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        answer -= num
    print(f"The Subtraction of the numbers is---> {answer}")

def mul(numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        answer *= num
    print(f"The Multiplication of the numbers is---> {answer}")

def div(numbers):
    if 0 in numbers[1:]:
        print("Error: Division by zero is not allowed, It is a Math error")
    else:
        answer = numbers[0]
        for num in numbers[1:]:
            answer /= num
        print(f"The Division of the numbers is---> {answer}")

def sqr(number):
    answer = number ** 2
    print(f"The Square of the number is---> {answer}")

# To keep looping until the user says stop
while True: 
    print("\nA. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Square")
    print("F. Exit")

    option = input("Input any option to perform a calculation---> ")

    if option in ["a", "A"]:
        print("Addition")
        count = int(input("How many numbers do you want to add? "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        add(numbers)

    elif option in ["b", "B"]:
        print("Subtraction")
        count = int(input("How many numbers do you want to subtract? "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        sub(numbers)

    elif option in ["c", "C"]:
        print("Multiplication")
        count = int(input("How many numbers do you want to multiply? "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        mul(numbers)

    elif option in ["d", "D"]:
        print("Division")
        count = int(input("How many numbers do you want to divide? "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        div(numbers)

    elif option in ["e", "E"]:
        print("Square")
        number = float(input("Input the number to square---> "))
        sqr(number)
    
    elif option in ["f", "F"]:
        print("Exiting the Calculator, Goodbye!!!")
        break
    
    cont = input("Do you want to continue? (yes/no)---> ")
    if cont.lower() != "yes":
        break
