a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
operator = input("Enter your operator (+,-,*,/) : ")

if(operator == '+'):
    print(a+b)
elif(operator == '-'):
    print(a-b)
elif(operator == '*'):
    print(a*b)
else:
    print(a/b)