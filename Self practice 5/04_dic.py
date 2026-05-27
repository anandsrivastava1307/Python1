# a = {
#     "key": "value",
#     "Anand": "code",
#     "marks": "100",
#     "list": [1, 2, 9]
# }
# print(a["key"]) # isse hume value milega jo key ke corresponding hai
# print(a["marks"]) # isse hume value milega jo key ke corresponding hai

a = {
    "name": "Anand Srivastava",
    "city": "Ayodhya",
    "marks": 100
}

# print(a.items()) # isse hume a dictionary ke sare key value pairs mil jayenge
# print(a.keys()) # isse hume a dictionary ke sare keys mil jayenge
a.update({"name": "Aditi Srivastava"})   # isse dictionary ke kisi key ka value update ho jayega
print(a) # isse hume updated dictionary mil jayega
 
print(a.get("name")) # isse hume name key ke corresponding value mil jayega
