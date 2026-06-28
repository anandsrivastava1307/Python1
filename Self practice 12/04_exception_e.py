try:
    x = int(input("Enter your number: "))
    print(10/x)

except Exception as e:
    print("Error", e)

else:
    print("Success")

finally:
    print("Program End")