friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
print(friends)

friends.append("Anand")  # Adds "Anand" to the end of the list
print(friends)

l1 = [1, 23, 12, 46, 24, 45, 43]
l1.sort() # Sorts the list in ascending order
print(l1)

l1.reverse() # Reverses the order of the list
print(l1)

l1.insert(2, 100) # Inserts 100 at index 3
print(l1)

print(l1.pop(2)) # Removes and returns the element at index 2 (which is 12 in this case)
print(l1) #or

value = l1.pop(2) # Removes and returns the element at index 2 (which is 12 in this case)
print(value) # Prints the removed value (12)
print(l1) # Prints the list after removing the element at index 2

l1.remove(45) # Removes the first occurrence of 45 from the list
print(l1)