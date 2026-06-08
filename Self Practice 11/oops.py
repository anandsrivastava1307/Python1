class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # def update_name(self, new_name):
    # self.name = new_name

class Student(Person):
    def __init__(self,name, age, roll_no, marks, grade):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.__marks = marks
        self.grade = grade

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def show_details(self):
        super().show_details()
        print(f"Roll no: {self.roll_no}\nMarks: {self.__marks} \nGrade: {self.grade}")

class Teacher(Person):
    def __init__(self,name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Subject: {self.subject} \n Salary: {self.salary}")

d1 = Student("Anand",19, 1402731021,98, "A+")
d2 = Teacher("Aditi", 24, "English", 150000)
d1.show_details()
# print(f"Marks: {d1.get_marks()}")
d1.set_marks(100)
print(d1.get_marks())
print("-" * 30)
d2.show_details()

        