# def sum(a,b):
#    s= a+b
#    return s

# print(sum(10,30))

# def printHello(name):
#    sr="Hello "+name
#    print(sr)

# printHello("Naveen")


# def averageOfThree(a,b,c):
#    sum=a+b+c
#    avg=sum/3
#    return avg

# print(averageOfThree(10,23,43))
# print(averageOfThree(10,10,20))

# Types of Function

# Build-in Functions
# User defined Function

# name="nIketan"
# print("hello","ram", sep="%")

# # if i want to print both name in single line
# print("Ram",end=" ")
# print("kajal")  


# default arguments

def printMul(a,b=4):
    mul=a*b
    return mul

# printMul() #printMul() missing 2 required positional arguments: 'a' and 'b'
# print(printMul()) #takes default value
# print(printMul(4,5)) #value passes in argument
# print(printMul(3))