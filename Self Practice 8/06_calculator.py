def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error"
    return a/b

num1 = float(input("Enter your number : "))
choice = input("Enter your choice +, -, *, / : ")
num2 = float(input("Enter your number : "))

if choice == '+':
    print(f"{num1}+{num2}={add(num1,num2)}")
elif choice == '-':
    print(f"{num1}-{num2}={substract(num1,num2)}")
elif choice == '*':
    print(f"{num1}*{num2}={multiply(num1,num2)}")
elif choice == '/':
    print(f"{num1}/{num2}={divide(num1,num2)}")

else:
    print("Wrong input")
