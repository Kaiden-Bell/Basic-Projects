# Simple 4 funct calculator, can be used to introduce functions in python.

# Adds two numbers and returns the value
def add(a, b):
    return a + b 

# Subtracts two numbers and returns the value
def sub(a, b):
    return a - b

# Multiplys two numbers and returns the value
def multiply(a, b):
    return a * b

# Divides two numbers determines if the denominator is 0, if it is, then return 0, otherwise return the value
def divide(a, b):
    if b == 0:
        print("Divison by 0 is invalid!")
        return 0
    else:
        return a / b

if __name__ == "__main__":    
    while True:

        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))

        operation = input("Please enter which operation you'd like to perform (+, -, *, /), type q to quit: ")

        match operation:
            case '+':
                res = add(num1, num2)
                print(res)
            case '-':
                res = sub(num1, num2)
                print(res)
            case '*':   
                res = multiply(num1, num2)
                print(res)
            case '/':
                res = divide(num1, num2)
                print(res)
            case 'q':
                break
            case _:
                print("Invalid expression, please try again!")