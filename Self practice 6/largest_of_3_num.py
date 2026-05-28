a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))

if(a>b and a>c):
    print("Larger number is a", a)

elif(b>a and b>c):
     print("Larger number is b", b)

else:
      print("Larger number is c", c)