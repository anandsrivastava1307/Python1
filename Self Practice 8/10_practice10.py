#1 से n तक सभी संख्याओं का योग निकालो।

num = int(input("Enter your number : "))

total = 0

for i in range(1,num+1):
    total = total + i
    
print("your number : ",total)

