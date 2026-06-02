f = open("file.txt")

# lines = f.readlines()  # readlines() returns a list of lines in the file
# line1 = f.readline() # readline() reads one line at a time and returns it as a string, including the newline character at the end of the line
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

#with while loop
line = f.readline()
while(line != ""):
    print(line)  # end="" is used to avoid adding an extra newline character after each line
    line = f.readline()


#with for loop
# for line in f:
#     print(line, end="")  # end="" is used to avoid adding an extra newline character after each line

f.close()