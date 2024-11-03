
import time  # Importing time module

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def division(a,b):
    if(b==0):
        return "Cannot divide by Zero"
    else:
     return a/b
    
while True:
 print("Select Your choice from given Given Option")

 print("1. Addition")
 print("2. Subtraction")
 print("3. Multiplication")
 print("4. Division")
 print("5. Exit")

 option= int(input("Enter your Choice: "))

 if(option ==5):
    print("GoodBye!......")
    break

 num1 = int(input("Enter first Number: "))
 num2 = int(input("Enter Second Number: "))



 if(option==1):
   sumValue= sum(num1,num2)
   print("Result = ", sumValue)
 elif(option==2):
    diffValue = sub(num1,num2)
    print( "Result = ", diffValue)
 elif(option==3):
    product=mul(num1,num2)
    print( "Result = ",  product)
 elif(option==4):
    divValue= division(num1,num2)
    print( "Result = ", divValue)
 else:
    print("Invalid Selection")

 time.sleep(2)

