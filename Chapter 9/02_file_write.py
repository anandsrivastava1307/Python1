st = "Hey Aditi you are amazing!"

f = open("myfile.txt", "w") # w stands for write mode, which allows you to create a new file or overwrite an existing file
f.write(st)
f.close()