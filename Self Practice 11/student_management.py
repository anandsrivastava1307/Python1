class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, marks, grade):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade

    def show_details(self):
        super().show_details()
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")


students = []


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    roll_no = int(input("Enter Roll No: "))
    marks = int(input("Enter Marks: "))
    grade = input("Enter Grade: ")

    student = Student(name, age, roll_no, marks, grade)

    students.append(student)

    print("Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("No Students Found")
        return

    for student in students:
        print("-" * 30)
        student.show_details()


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")