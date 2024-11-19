class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        

    def get_Average(self):
        Sum=0
        for val in self.marks:
            Sum +=val
         
        print(f"hi {self.name}, your average marks is {Sum//3}")

    @staticmethod #decorator(a decorator is used to change the behaviour of normal function)
    def hello():
        print("Hello programmer")



marks_List=[96,97,97]
s1=Student("Niketan",marks_List)

s1.get_Average()
s1.hello()

# For pillars of oops concept i.e 
# 1. Abstraction -> Hiding the implementation details of a class and only showing the essential features to the user.
# 2. Encapsulation -> Wrapping data and function into a single unit(object)
# 3. Inheritance
# 4. Polymorphism