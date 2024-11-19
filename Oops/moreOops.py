# class Student:

#     college_name= "Hierank Business school" # class attribute

#     def hello(self):
        
#         print("Hello Student")


# s1 = Student()
# s1.hello()
# print(s1.college_name)
# print(Student.college_name)


# Another Example

class Student:

    college_name= "Hierank busines school"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print("Welcome Student",self.name)
    
    def get_marks(self):
        return self.marks



s1= Student("Niketan",45)

s1.welcome()
print(s1.get_marks())