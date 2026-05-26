a = (1, 45, 342, 3424, False, "Rohan", "Shivam")
print(a)


no = a.count(45) # Counts the number of occurrences of 45 in the tuple
print(no) # Output: 1

my_tuple = (1, 2, 2, 3, 4)

# count()
print(my_tuple.count(2))  # output is 2 because 2 appears twice in the tuple

# index()
print(my_tuple.index(3))   # output is 3 because 3 is at index 3 in the tuple

print(len(my_tuple)) # Output: 5, because there are 5 elements in the tuple