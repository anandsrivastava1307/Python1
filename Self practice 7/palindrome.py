name = input("Enter your word : ")

if name == name[::-1]:
    print(name, "is a palindrome")

else:
    print(name, "is NOT a palindrome")