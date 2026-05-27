#Questions 1:
nums = [1, 1, 2, 2, 3, 4]
unique = set(nums) # isse hume nums list ke unique elements mil jayenge
print(unique) # isse hume unique set mil jayega

#Question 2:
a = {1, 2, 3, 4}
b = {3, 4}
unique = a.difference(b) # isse hume set a me se set b ke unique elements mil jayenge
print(unique) # isse hume unique set mil jayega

#Question 3:
a = {1, 2}
b = {2, 3, 4}
unique = a.union(b) # isse hume set a me se set b ke unique elements mil jayenge
print(unique) # isse hume unique set mil jayega

#Question 4:
required_subjects = {"Math", "English"}
student_subjects = {"Math", "English", "Science"}
print(required_subjects.issubset(student_subjects)) # isse hume pata chalega ki required_subjects set student_subjects set ka subset hai ya nahi
