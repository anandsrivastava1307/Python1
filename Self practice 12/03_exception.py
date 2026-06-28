try:
    num = int(input("Enter your number: "))
    print(10/num)

except ValueError:
    print("Number enter karo")

except ZeroDivisionError:
    print("Division by zero not allowed")