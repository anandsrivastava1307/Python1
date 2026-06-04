class Student:  
    def __init__(self,name,grade,percentage,team):  #method
        self.name = name #attribute
        self.grade = grade #attribute
        self.percentage = percentage #attribute
        self.team = team

    def student_details(self): #method
        print(f"{self.name} is in class {self.grade} with {self.percentage}% is in team {self.team}")

team1 = 'A'
team2 = 'B'
#object - instance of class
student1 = Student('Anand', 12, 96, team1)
# print(student1.name, student1.grade)

student2 = Student('Aditi', 10, 98, team2)
# print(student2.name, student2.grade)

student1.student_details()
student2.student_details()
# print(student1.team)
