def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")
    
def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")
    
def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")
    
def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")
    
    
operation = input("Enter 'A' for Addition, 'S' for Subtration, 'M' for Multiplication, 'D' for Division ").upper()
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

if operation == "A":
    add(a, b)
elif operation == "S":
    sub(a, b)
elif operation == 'M':
    mul(a, b)
elif operation == 'D':
    div(a, b)
    

