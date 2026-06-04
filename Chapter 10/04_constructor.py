class Employee:
    language = "Python"  #This is a class attribute
    salary = 1200000   #attribute

    def __init__(self, name, salary, language):  #dunder method which is automatically called
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

anand = Employee("Anand", 130000, "Javascript")  #anand = object
# anand.name = "Anand"
print(anand.name, anand.salary, anand.language)
