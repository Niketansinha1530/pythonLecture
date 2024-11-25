# my_list = [10,"Python",5.5]

# print(my_list)

# first_element = my_list[0]
# print(first_element)

# last_element = my_list[len(my_list)-1] #we can also use negative index my_list[-1]
# print(last_element)

# try:
#     not_defined_index = my_list[6]
#     print(not_defined_index)
# except IndexError:
#     print("Index out of bounds!")


# my_list = [10,"Python",5.5]

# #Slice and print the first two elements.
# print(my_list[0:2])
# #Slice and print everything except the first element.
# print(my_list[1:])

# #Reverse the list using slicing.
# reverse_list=my_list[::-1] #reverse list by slicing
# print(reverse_list)

# my_list = [10,"Python",5.5]

# my_list.append("Hello")
# print(my_list)


# my_list.insert(1,20)
# print(my_list)

# my_list.remove("Python")
# print(my_list)

# num_of=my_list.count(10)
# print(num_of)


my_list = [10, 20, 5.5, "Hello"]

numeric_values = [x for x in my_list if isinstance(x,(int,float))]
numeric_values.sort()
print("Ascending order: ", numeric_values)

reverse_numeric_value= [x for x in my_list if isinstance(x,(int,float))]
reverse_numeric_value.sort(reverse=True)
print("Descending order: ",reverse_numeric_value) 


my_list.clear()

print(my_list)
my_list.append("Niketan")
print(my_list)




# The isinstance() function in Python is used to check if an object belongs to a specific class or a tuple of classes. It’s a built-in function that returns True if the object matches the specified type(s) and False otherwise.
# x = 5.4
# print(isinstance(x,(int,float)))

