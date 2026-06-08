class Employee:    #Base class
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):   #Derived or Child class
    company = "ITC Infotech"
    def showLanguage(self,language):
        self.language = language
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()
b.show("Anand", 1500000)
b.showLanguage("Python")
print(a.company, b.company)
