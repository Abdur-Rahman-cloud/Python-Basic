# PART A
name = "Abdur Rahman"
print(name)

age = 23
height = 5.6
print(age)
print(height)

No = 45
print(type(No))

is_student = True
print(is_student)

Number = int(input("enter a No"))
print(Number)


# PART B
a = int(input("enter value of a"))
b = int(input("enter value of b"))
print(a+b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)

if num2 > num1:
    print(num2, "is greater than", num1)


num = int(input("Enter a number: "))
# Check even or odd
if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")


# Take marks as input
marks = int(input("Enter your marks: "))
# Check pass or fail
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# Take a number as input
num = int(input("Enter a number: "))
# Check conditions
if num < 10:
    print("The number is less than 10")
elif num == 10:
    print("The number is equal to 10")
else:
    print("The number is greater than 10")

# Mini Project
num = int(input("Enter a number: "))
# Check if the number is positive or negative
if num >= 0:
    print("The number is Positive")
else:
    print("The number is Negative")
