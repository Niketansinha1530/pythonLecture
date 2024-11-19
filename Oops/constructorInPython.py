# class person:

#     def __init__(self,name,age):
#         print(self)
#         self.name=name
#         self.age=age

#     def info(self):
#         print(f"my name is {self.name} and i am {self.age} old")


# p1 = person("Niketan",21)

# p1.info()

# p2 = person("Buddy",22)
# p2.info()

#Multiple arguments

class Shape:
    def __init__(self, *args):
        if len(args) == 1:  # Circle with radius
            self.shape = "Circle"
            self.radius = args[0]
        elif len(args) == 2:  # Rectangle with width and height
            self.shape = "Rectangle"
            self.width, self.height = args
        elif len(args) == 3:  # Cuboid with lenght,wideth and height
            self.shape = "Cuboid"
            self.width, self.length, self.height = args
        else:
            self.shape = "Unknown"

    def display(self):
        if self.shape == "Circle":
            print(f"Shape: {self.shape}, Radius: {self.radius}")
        elif self.shape == "Rectangle":
            print(f"Shape: {self.shape}, Width: {self.width}, Height: {self.height}")
        elif self.shape == "Cuboid":
            print(f"Shape: {self.shape}, Width: {self.width}, Height: {self.height},Lenght:{self.length}")
        else:
            print("Unknown shape")

# Example usage
circle = Shape(10)           # Circle with radius 10
rectangle = Shape(20, 30)     # Rectangle with width 20 and height 30
cuboid = Shape(10,20,30)    #Cuboid

circle.display()     # Output: Shape: Circle, Radius: 10
rectangle.display()  # Output: Shape: Rectangle, Width: 20, Height: 30
cuboid.display()
