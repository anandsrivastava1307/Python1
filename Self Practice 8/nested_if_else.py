num = int(input("Enter your number : "))

if num > 0:
    if num%2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")

else:
    print(f"{num} is negative number.")