# Create a program that will ask for grade percentage.
# Display the equivalent grade/mark and description
# Example: Input grade: 87.6 Grade/Mark: 1.75 Description: Very Good

import math

rawGrade = float(input("Enter your grade percentage here: "))
grade = math.ceil(rawGrade)

if(grade >= 97 and grade <= 100):
    print("Mark: 1.0")
    print("Description: Excellent")
elif(grade >= 94 and grade <= 96):
    print("Mark: 1.25")
    print("Description: Excellent")
elif(grade >= 91 and grade <= 93):
    print("Mark: 1.5 ")
    print("Description: Very Good")
elif(grade >= 88 and grade <= 90):
    print("Mark: 1.75")
    print("Description: Very Good")
elif(grade >= 85 and grade <= 87):
    print("Mark: 2.0")
    print("Description: Good")
elif(grade >= 82 and grade <= 84):
    print("Mark: 2.25")
    print("Description: Good")
elif(grade >= 79 and grade <= 81):
    print("Mark: 2.5")
    print("Description: Satisfactory")
elif(grade >= 76 and grade <= 78):
    print("Mark: 2.75")
    print("Description: Satisfactory")
elif(grade == 75):
    print("Mark: 3.0")
    print("Description: Passing")
else:
    if(grade >= 65 and grade <= 74 ):
        print("Mark: 5.0 ")
        print("Description: Failure")