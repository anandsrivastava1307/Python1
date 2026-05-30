# name = input("Enter your name :")
# age = int(input("Enter your age : "))

# retirement_age = 60
# age_left = retirement_age - age

# print("Hello", name)
# print("Your age is :", age)
# print("Age left : ", age_left)

try:
    age = int(input("Umar batao: "))
    print("Your age is : ", age)


except ValueError:
    print("Wrong input")
