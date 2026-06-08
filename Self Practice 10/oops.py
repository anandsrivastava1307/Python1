# OOPs(Object oriented programming) in python

# using Lists - creating students record
# student record

# student_1 = ['Anand', 10] #Name, Grade
# student_2 = ['Aditi', 12]

# print(f"{student_1[0]} is in class {(student_1[1])}")
# print(f"{student_2[0]} is in class {(student_2[1])}")

#using OOPs creating student record

#class - blueprint or template
#__init__ method- constructor value initialize-fix
#self parameter - reference or connection btw class and object - fix
#class name(Student) start with capital word
class Student:  
    def __init__(self,name,grade,percentage):  #method
        self.name = name #attribute
        self.grade = grade #attribute
        self.percentage = percentage #attribute

    def student_details(self): #method
        print(f"{self.name} is in class {self.grade} with {self.percentage} percentage")

#object - instance of class
student1 = Student('Anand', 12, 96)
#print(student1.name, student1.grade)

student2 = Student('Aditi', 10, 98)
#print(student2.name, student2.grade)

student1.student_details()
student2.student_details()
# print(student1.name)

# print(student1.__dict__)
# print(student1.percentage)
'''Modify object properties(attribute)'''
'''student1.percentage = 99  #modify
print(student1.percentage)'''

#Delete object property
'''print(student1.__dict__)
del student1.percentage
print(student1.__dict__)'''

#Delete object
del student1
print(student1)








