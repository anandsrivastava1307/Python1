word = input("Enter a word : ").lower()

if word == word[::-1]:
    print(word, "Palindrome")

else:
    print(word, " NOT Palindrome")

