class Employee:
    language = "Python"  #This is a class attribute
    salary = 1200000   #attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

anand = Employee()  #anand = object
anand.language = "Javascript" # This is an instance attribute
anand.getInfo() #Employee.getInfo(anand)
