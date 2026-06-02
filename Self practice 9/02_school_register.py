while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")

        with open("students.txt","a") as f:
            f.write(name + "\n")

    elif choice == "2":
        with open("students.txt","r") as f:
            print(f.read())

    elif choice == "3":
        break