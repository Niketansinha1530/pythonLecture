import cmath as m

# Find the sum of two numbers

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter Second number: "))
# sum = num1 + num2
# print(f"Sum of {num1} and {num2} is {sum}")

# Find Square Root of Real Number

# num = float(input("Enter any number: "))
# # sqrt = num ** 0.5
# # print(f"Square root of {num} is {sqrt}")
# sqrt = m.sqrt(num)
# print(f"Square root of {num} is {sqrt}")

# Find the area of a triangle

# base = float(input("Enter the base of the triangle : "))
# height = float(input("Enter the height of the triangle : "))
# area = 0.5 * base * height
# print(f"Area of the triangle is {area}")

# Solve Quadratic Equation
# ax^2 + bx + c = 0

# a = int(input("Enter the value of a where a!=0 : "))
# b = int(input("Enter the value of b : "))
# c =int(input("Enter the value of c: "))

# d = b**2 - 4*a*c
# root1 = (-b + m.sqrt(d)) / 2*a
# root2 = (-b - m.sqrt(d)) / 2*a

# print(f"Root1: {root1.real} and Root2: {root2.real}")

# Swap two numbers
#method 1
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter Second number: "))
# print(f"Number1: {num1} and Number2: {num2}")
# temp = num1
# num1 = num2
# num2 = temp
# print(f"Number1: {num1} and Number2: {num2}")

#method 2
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter Second number: "))

# print(f"Number1: {num1} and Number2: {num2}")
# num1 = num1 + num2 #num1 = 10+20 = 30
# num2 = num1 - num2 #num2 = 30-20 = 10
# num1 = num1 - num2 #num1 = 30-10 = 20
# print(f"Number1: {num1} and Number2: {num2}")

# method 3
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter Second number: "))
# num1,num2 = num2,num1
# print(f"Number1: {num1} and Number2: {num2}")

# Generate a random number
import random as r
num = r.randint(0,100)
print(num)

