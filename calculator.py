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

    choice=input("Enter choice (1/2/3/4): ")

    if choice not in ['1','2','3','4']:
        print("Invalid choice")
        return

    if choice =='1':
        result=add(first_num,sec_num)
        operation='+'

    elif choice =='2':
        result=subtract(first_num,sec_num)
        operation='-'
    elif choice =='3':
        result=multiply(first_num,sec_num)
        operation='*'
    elif choice=='4':
        result=divide(first_num,sec_num)
        operation='/'

    print(f"\nResult: {first_num} {operation} {sec_num} ={result}")

if __name__=="__main__":
    calculator()


