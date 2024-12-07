
# Star printing
# row=6

# for i in range(1,row):
#     print("*"*i)

# Reverse Star Printing

# row =5
# count =4
# for i in range (1,row):
#     if(count>0):
#      print("*" *count)
#      count -=1

# Number Pyramid

# row =6
# count=1
# for i in range(1,row):
#     if(count<=6):
#      print(f"{i}"*count)
#      count +=1


# Sum of First N Numbers

# n = int(input("Enter the Number "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i

# print("sum of first n number is : ",sum)


#  Multiplication Table

# num = int(input("Enter any number: "))

# for i in range(1,11):
#     print(f"{num} * {i} = ",num*i)

# Count Even and Odd Numbers

# numbers = [12, 7, 19, 4, 8, 15, 23, 42,3,2]

# evenCount=0
# oddCount=0

# for el in numbers:
#     if(el%2==0):
#         evenCount +=1
#     else:
#         oddCount +=1

# print(f"Total number of EvenNUmber {evenCount}, Total number of OddNumber: {oddCount}")

# Factorial of a Number

n = int(input("Enter any Number: "))
fact =1
for i in range(1,n+1):
    fact = fact * i

print("Factorial of Number:  ",fact)


# List Squaring

# numbers = [2, 4, 6, 8]
# newNumber = []

# for el in numbers:
#     newNumber.append(el**2)

# print(newNumber)