friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]

print(friends[0])  # Apple

friends[0] = "Mango"
print(friends[0])  # Mango #Unlike strings, lists are mutable. We can change the value of a list item using its index.
print(friends[6])  # Rohan
print(friends[-1])  # Rohan #Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item and so on.
print(friends[-2])  # Akash

print(friends[1:5])  # ["Orange", 5, 345.06, False]