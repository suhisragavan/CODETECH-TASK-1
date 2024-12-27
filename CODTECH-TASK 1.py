def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Welcome to the Basic Calculator!")
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Get user input for operation
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number corresponding to the operation: ")

    if operation == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} = {result}")
    else:
        print("Invalid operation selected!")

if __name__ == "__main__":
    main()