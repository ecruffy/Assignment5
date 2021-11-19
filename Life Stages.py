# Create a program that ask for an age of a person and then display the life stage of person
# Rules:
# 0-12: Kid
# 13-17: Teen
# 18: Debut
# 19 and above: Adult

print("Please enter your age to determine your life stage")
age = int(input("Age: "))

if(age >= 0 and age <= 12):
    print("Kid")
elif(age >= 13 and age <=17):
    print("Teen")
elif(age == 18):
    print("Debut")
else:
    print("Adult")
