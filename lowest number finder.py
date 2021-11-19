# Create a program that ask 3 numbers
# Find the lowest number using only if-else statements
# Display the lowest number

print("This is a program that finds the lowest number out of the 3 you enter")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))

if(num1<num2 and num1<num3):
    print("{} is the lowest number".format(num1))
elif(num2<num3):
    print("{} is the lowest number".format(num2))
else:
    print("{} is the lowest number".format(num3))