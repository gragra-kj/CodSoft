def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error: You can't divide by zero"
    return x/y

def calculator():
    print("Simple calculator")
    first_num=float(input("Enter the first number: "))
    sec_num=float(input("Enter the second number: "))

    print("\nSelect your operation of choice ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
