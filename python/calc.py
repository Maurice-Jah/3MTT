
# A simple calculator 

def add():
    first_number = int( input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    sum = first_number + second_number
    print(f"The sum of {first_number} and {second_number}: {sum}")

def subtract():
    first_number = int( input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    subtract = first_number - second_number
    print(f"The substraction of {first_number} and {second_number}: {subtract}")

def multiply():
    first_number = int( input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    multiply = first_number * second_number
    print(f"The multiplication of {first_number} and {second_number}: {multiply}")


def divide():
    first_number = int( input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    divide = first_number / second_number
    print(f"The division of {first_number} and {second_number}: {divide}")

quesition = input("What do you want to calculate today? Press Enter to continue")
choice = input("Choose from one of the options ('+', '/', '*', or '-') ")

if(choice == '+'):
    add()
elif(choice == '-'):
    subtract()
elif(choice == '/'):
    divide()
elif(choice == '*'):
    multiply()
else:
    input("Kindly choose from one of these options ('+', '/', '*', or '-') ")

