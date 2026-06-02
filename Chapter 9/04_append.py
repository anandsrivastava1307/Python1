st = " Hey Anand you are amazing!"

f = open("myfile.txt", "a")  # "a" stands for append mode, which allows you to add
#new content to the end of the file without overwriting the existing content

f.write(st)
f.close()