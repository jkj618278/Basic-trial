# Simple Calculator

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    
    if op == 'q':
        break

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        print("Result:", num1 / num2 if num2 != 0 else "Error")
    else:
        print("Invalid")