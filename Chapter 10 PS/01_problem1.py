# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Anand", 1200000, 224001)
print(p.name, p.salary, p.pin, p.company)

r = Programmer("Aditi", 1300000, 224001)
print(r.name, r.salary, r.pin, r.company)
