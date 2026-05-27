marks = {
    "Anand": 100,
    "Aditi": 56,
    "Rohit": 23,
}

# print(marks.items()) #prints the key value pair in the form of list of tuples like [('Anand', 100), ('Aditi', 56), ('Rohit', 23)]
# print(marks.keys()) #prints the keys of the dictionary in the form of list like Anand, Aditi, Rohit
# print(marks.values()) #prints the values of the dictionary in the form of list like 100, 56, 23

# marks.update({"Anand": 99,"Sonia": 78}) #marks update and new student added 
# print(marks)

print(marks.get("Anand2")) #pRINTS nONE because there is no key "Anand2" in the dictionary
print(marks["Anand2"]) #printss KeyError because there is no key "Anand2" in the dictionary
