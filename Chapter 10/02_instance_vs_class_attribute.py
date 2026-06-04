class Employee:
    language = "Python"  #This is a class attribute
    salary = 1200000   #attribute

anand = Employee()  #anand = object
anand.language = "Javascript" # This is an instance attribute
print(anand.language, anand.salary)
