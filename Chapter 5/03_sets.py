s = {1, 5, 32}

e = set() #Don't use s = {} as it will create an empty dictionary, not a set

s = {1, 5 , 32, 54, 5, 5, 5} #Duplicates are not allowed in sets, so the set will only contain unique values
# print(s) #Output: {1, 5, 32, 54}

s = sorted(s) #Sets are unordered, so this will not change the order of the elements in the set
print(s) #Output: [1, 5, 32, 54]