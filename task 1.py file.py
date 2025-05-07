#Basic mathematical operation program
#taking two number as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number:  "))

#perform the operation
addition = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2

#to avoid division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division:"unidentified(cannot divide by zero)"


# the result
print("\nresults: ")
print("addition: ",addition)
print("substraction: ",substraction)
print("multiplication: ",multiplication)
print("division: ",division)