# class Student:
#     name="Niketan"


# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2)

# In Python, you cannot define multiple constructors in the same class the way you might in languages like Java or C++ (where method overloading is allowed).

# Why?
# Python doesn't support method overloading because a class can have only one method with a given name. If you define multiple __init__ methods, the last one defined will override the previous ones.



class cars:

    def __init__(self):
        print(self) #print address of the class.
        print("Hello i am car Class object")


c1 = cars()
print(c1)