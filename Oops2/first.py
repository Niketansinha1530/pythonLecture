# Private(Like) attributes & Methods

# conceptual Implementaions in Python
# Private attributes & methods are meant to be used only within the class and are not accessible from outside the class.

# Make things private we need to use underscore underscore with vairalbe or method name __name 

#Private variable and Method

# class Account:

#     __ac_ifsc="AB32CD" #private variable
#     name="Ram"

#     def __hello(self): # private method
#         print("hello Customer")


# print(Account.name)
# print(Account.__ac_ifsc)

#Single level Inheritance

# class Car:

#     @staticmethod
#     def start():
#         print("Car Started......")
    
#     @staticmethod
#     def stop():
#         print("Car Stoped")

# class Toyota(Car): #inheritance

#     def __init__(self,name):
#         print("Name: ",name)

# c1 = Toyota("Fortuner")
# c1.start()

# c2= Toyota("Innova")
# c2.start()


#Multilevel inheritance

#Multiple inheritance

class A:
    varA= "Welcome to class A"

class B:
    varA= "Welcome to class B"

class C(A,B):
    varC= "Welcome to class C"

c = C()
print(c.varC)
# print(c.varB)
print(c.varA)
