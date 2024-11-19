class Student:
    # Constructor with default arguments
    def __init__(self, name=None, role_no=None, mobile_no=None, age=None):
        self.name = name
        self.role_no = role_no
        self.mobile_no = mobile_no
        self.age = age
        print(name, role_no, mobile_no, age)


s1 = Student("Niketan", 21, 9560912059, 21)
s2 = Student("Ranjana", 23, 8287801017, 20)
