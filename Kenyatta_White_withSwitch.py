# kenyatta's calculator
# subtract, divide, multiply, divide, exponent, square root
import math
print("Welcome to Kenyatta's Kalculator")
switch = {1:'subtract', 2:'add', 3:'multiply', 4: 'divide', 5:'exponent', 6:'square root'}

def operation(Operation_Choice):
    print(switch(1))
    print(switch(2))
    print(switch(3))
    print(switch(4))
    print(switch(5))
    print(switch(6))
    
def subtract (x, y):
    return x - y
def add (x, y):
    return x + y
def multiply (x, y):
    return x * y
def division (x, y):
    return x/y
def exponent (x, y):
    return x **y

while True:
    choice=input ("Select your operation. (1/2/3/4/5/6): ")
    if choice in ( '1','2', '3', '4', '5', '6'):
        try:
            num1= float(input("Enter your first number: "))
            num2= float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input. Please enter a NUMBER.")
            continue
        if choice =='1':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '2':
            print(num1,"+", num2, "=", add(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", exponent(num1, num2))
        elif choice == '6':
            print(math.sqrt(num1))
        