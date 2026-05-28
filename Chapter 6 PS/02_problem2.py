# Question2: Write a program to find out whether a student has passed or failed if it requires a total of 40% and ar least 33% in each subject to passs. Assume 3 subjects and take marks as an input from the user.

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))

# Check for total percentage
total_percentage = (subject1 + subject2 + subject3)/300 * 100

if (total_percentage>=40 and subject1>=33 and subject2>=33 and subject3>=33):
        print("Congratulations! You have passed.", total_percentage)
else:
        print("Sorry! You have failed due to low marks in one or more subjects.", total_percentage)
