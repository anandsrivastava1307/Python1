s = {1, 5 , 32, 54, 5, 5, 5, "Anand"} 

print(s, type(s)) #Output: {1, 5, 32, 54, 'Anand'} <class 'set'>

s.add(100) #Adds an element to the set
print(s, type(s)) #Output: {1, 5, 32, 54, 'Anand', 100} <class 'set'>

s.update([200, 300, 400]) #Adds multiple elements to the set
print(s, type(s)) #Output: {1, 5, 32, 54, 'Anand', 100, 200, 300, 400} <class 'set'>

s.remove(5) #Removes an element from the set. If the element is not present, it will raise a KeyError
print(s)

s.discard(32) #Removes an element from the set. If the element is not present, it will do nothing
print(s)