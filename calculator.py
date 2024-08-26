import math

def addition(numbers):
    answer = sum(numbers)
    print(f"The addition of the numbers is---> {answer}")

def subtraction(numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        answer -= num
    print(f"The subtraction of the numbers is---> {answer}")

def multiplication(numbers):
    answer = numbers[0]
    for num in numbers[1:]:
        answer *=num
    print(f"The multiplication of the numbers are---> {answer}")

def division(numbers):
    if 0 in numbers[1:]:
        print("Error: Division by zero is not allowed, It is a math error")
    else:
        answer = numbers[0]
        for num in numbers[1:]:
            answer /num
        print(f"The division of thre number is---> {answer}")

def square(numbers):
    answer = numbers **2
    print(f"The square of the number is---> {answer}")

def square_root(numbers):
    answer = math.isqrt(numbers)
    print(f"The square root of the number is---> {answer}")

def factorial(numbers):
    answer = math.factorial(numbers)
    print(f"The fcatorial of the number is ---> {answer}")

while True:
    print("...Welcome To The Calculator...\n")
    print("...Select the following mathematical operations...")
    print("\nA. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Square")
    print("F. Square Root")
    print("G. Factorial")
    print("H. Exist")

    options = input("Input any options to perform operation on---> ")
    if options in ["a", "A", "addition.lower()"]:
        print("...Addition...")
        count = int(input("How many numbers do you want to add?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        addition(numbers)

    elif options in ["b", "B", "subtraction.lower()"]:
        print("...Subtraction...")
        count = int(input("How many numbers do you want to subtract?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        subtraction(numbers)

    elif options in ["c", "C", "multiplication.lower()"]:
        print("...Multiplication...")
        count = int(input("How many numbers do you want to multiply?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        multiplication(numbers)

    elif options in ["d", "D", "division.lower()"]:
        print("...Division...")
        count = int(input("How many numbers do you want to divide?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        division(numbers)

    elif options in ["e", "E", "square.lower()"]:
        print("...Square...")
        count = int(input("How many numbers do you want to find the square?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        square(numbers)

    elif options in ["f", "F", "square_root.lower()"]:
        print("...Square Root...")
        count = int(input("How many numbers do you want to find the square root?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        square_root(numbers)

    elif options in ["g", "G", "factorial.lower"]:
        print("...Factorial...")
        count = int(input("How many numbers do you want to perform factorial?---> "))
        numbers = [float(input(f"Input number {i+1}---> ")) for i in range(count)]
        factorial(numbers)

    elif options in ["h", "H", "exist.lower"]:
        print("...Existing the Calculator, Goodbye!!!. Have a Wonderful Day")
        quit()

    contd = input("Do you want to continue with the calculator? (yes/no)---> ")
    if contd.lower() != "yes":
        break

