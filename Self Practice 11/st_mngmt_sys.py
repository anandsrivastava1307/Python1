from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractmethod
    def show_details(self):
        print(f"Name: {self.name} \nAge: {self.age}")

    def greet(self):
        print("Welcome to School")

class Student(Person): #Inheritance
    def __init__(self, name,age,roll_no,marks):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.__marks = marks   #__marks = Encapsulation

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        self.__marks = marks

    def show_details(self):
        super().show_details()
        print(f"Roll no: {self.roll_no}")
        print(f"Marks: {self.__marks}")

class Teacher(Person):
    def __init__(self,name,age, subject, salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    def show_details(self):
        super().show_details()
        print(f"Subject: {self.subject}")
        print(f"Salary: {self.salary}")
    
s = Student("Anand", 19,1402731021,95)
s.get_marks()
s.set_marks(90)
s.get_marks()
t = Teacher("Aditi", 24, "English", 150000)

# s.greet()
# s.show_details()

# print("-"*30)

# t.greet()
# t.show_details()

people = [s, t]  #Polymorphism
for person in people:
    person.show_details()
    print("-" * 20)
