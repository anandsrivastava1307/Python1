class Employee:
    language = "Py"  #This is a class attribute
    salary = 1200000   #attribute

anand = Employee()  #anand = object
anand.name = "Anand" # This is an instance attribute
print(anand.name, anand.language, anand.salary)

aditi = Employee()
aditi.name = "Aditi"
print(aditi.name, aditi.salary, aditi.language)

'''Here name is instance attribute and salary and language are class attributes as they 
directly belong to the class'''