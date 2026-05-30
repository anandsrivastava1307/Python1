sentence = "madam like racecar and civic"

words = sentence.split()

for word in words:
    if word == word[::-1]:
        print(word, "Palindrome")
    else:
        print(word, "Not Palindrome")

        