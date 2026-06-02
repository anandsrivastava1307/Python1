# f = open("file.txt")
# print(f.read())
# f.close()

#The same code can be written using with statement as follows:

with open("file.txt") as f:
    print(f.read())

#tumhe file close karne ki zarurat nhi hai with statement automatically file ko close kar deta hai after the block of code is executed.