def calculator():
    
    num1 = float(input("Enter the first number:"))
    
    num2 = float(input("Enter the second number:"))
    
    print("Choose an operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Multi")
    print("4. Div")

    operation = input("Enter the number for the operation: ")

    if operation == '1':
        result = num1 + num2
    elif operation == '2':
        result = num1 - num2
    elif operation == '3':
        result = num1 * num2
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "It is undefined."
    else:
        result = "Invalid operation."

    print(f"The result is: {result}")

calculator()