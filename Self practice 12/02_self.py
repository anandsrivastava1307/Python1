class Student:
    def __init__(self,name):
        self.name = name
        print("__init__ called")

    def __str__(self):
        return f"Student Name: {self.name}"

s = Student("Anand")
print(s)