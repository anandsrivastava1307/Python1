note = input("Enter note: ")

with open("notes.txt","a") as f:
    f.write(note + "\n")

print("Note Saved")