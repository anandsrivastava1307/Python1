'''Without Walrus 
name = input("Enter name: ")

while name != "quit":
    print("Hello", name)
    name = input("Enter name: ") '''

# With Walrus Operator

while (name := input("Enter name: ")) != "quit":
    print("Hello", name)