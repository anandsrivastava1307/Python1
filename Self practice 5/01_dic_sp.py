student = {
    "Name": "Anand Srivastava",
    "City": "Ayodhya",
    "Age": 20
}

# print(student.get("City")) # output me Ayodhya aayega
    
# student.update({"City": "Lucknow"}) # isse city ka value update ho jayega                                         

# print(student.values()) # isse hume student ke sare values mil jayenge

# print(student.keys()) # isse hume student ke sare keys mil jayenge

student.pop("Age") # isse age key aur uska value delete ho jayega
print(student) # isse hume student dictionary ka updated version mil jayega