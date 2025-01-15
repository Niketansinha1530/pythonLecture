
#Convert km into miles

# km = float(input("Enter your value in kms: "))
# miles = km * 0.621371
# print(f"{km} km is equal to {miles} miles")

#project 
# distance = float(input("Enter the distance to be travelled: "))

# print(" ****\t In Which Mesurement you want to convert the distance?\t*** ")
# print("1. Kilometers to Miles")
# print("2. Miles to Kilometers")

# choice =int(input("Enter your choice: "))
# if choice == 1:
#     miles = distance * 0.621371
#     print(f"{distance} km is equal to {miles} miles")
# elif choice == 2:
#     km = distance * 1.60934
#     print(f"{distance} miles is equal to {km} km")
# else:
#     print("Invalid Choice")

# convert temperature from celsius to fahrenheit
# celcius = float(input("Enter the temerature in celcius:"))

# fahrenheit = (celcius *1.8) + 32

# print(f"{celcius} celcius is equal to {fahrenheit} farhenheit")

# check if a number is positive, negative or zero

# num = float(input("Enter any number to check a number is positive, negative or Zero: "))

# if num < 0 :
#  print("Number is negative")
# elif num>0 :
#  print("Number is poistive")
# else :
#  print ("Your Number is Zero")

# num = int(input("Enter a number: "))

# if num%2==0:
#     print(f"{num} is a Even Number ")
# else: 
#     print(f"{num} is a Odd Number ")


# num1 = int(input("Enter first Number: "))
# num2 = int(input("Enter second Number: "))
# num3 = int(input("Enter third Number: "))

# if num1 > num2 and num1 > num3:
#  print(f"{num1} is greater than {num2} and {num3}")
# elif num2> num1 and num2 > num3:
#  print(f"{num2} is greater than {num1} and {num3}")
# else :
#  print(f"{num3} is greater than {num1} and {num2}")

# check a number is prime or not

num = int(input("Enter a number: "))
count =0
for i in range(2,num):
    if num % i ==0:
        count = count +1
        break


if(count == 0):
    print(f"{num} is a prime number")
else:    
    print(f"{num} is not a prime number")