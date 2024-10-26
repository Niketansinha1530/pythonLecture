# ********************************           Introduction of List        *********************************************

# In Python, a list is a collection of items (also called elements). These items can be of different types, such as integers, strings, or even other lists. Lists are mutable, meaning you can change the content after the list has been created.

# Key Features of Lists:
# Ordered: Items have a defined order and can be accessed by their position (index).
# Mutable: You can modify a list after it's created.
# Dynamic: Lists can grow or shrink as needed.
# Heterogeneous: A list can contain elements of different types.


# *****************************************     List    *************************************

myList = [1,2,3,"hello", 2.5,True]

print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])
# print(myList[5])
 
myList[5]=False

print(myList)

# Append: Adds an element at the end of the list.
myList.append("Niketan")
print(myList)

#Insert: Adds an element at a specific position.
myList.insert(0,7)
print(myList)

# Remove: Removes the first occurrence of a value.

myList.remove("Niketan")
print(myList)

# Pop: Removes an element by index (default is the last element) and returns it.

last_value=myList.pop() # we can also pass indexes for removing element
print(last_value)
print(myList)

print("****************************")

carList = ["BMW","VOLVO","MAHINDRA","TATA","TESLA"]

# print(carList[1:3])
ListOfCar = carList[1:3]
ListOfCar.append("Maruti")
print(ListOfCar)

print(carList[0:])
print(carList[-1])