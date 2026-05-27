s1 = {1,45, 6}
s2 = {7, 8, 1, 78}

print("union", s1.union(s2)) #Output: {1, 6, 7, 8, 45, 78} - Returns a new set that is the union of s1 and s2
print("intersection", s1.intersection(s2)) #Output: {1} - Returns a new set that is the intersection of s1 and s2
print("difference", s1.difference(s2)) #Output: {6, 45} - Returns a new set that is the difference of s1 and s2 (elements in s1 but not in s2)

print({1}.issubset(s1)) #Output: True - Returns True if {1} is a subset of s1
print(s1.issuperset({1, 6})) #Output: True - Returns True if s1 is a superset of {1}