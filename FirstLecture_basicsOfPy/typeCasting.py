# # Converting float to int
# num_float = 10.5
# num_int = int(num_float)
# print(num_int)  # Output: 10

# # Converting string to int
# num_str = "123"
# num_int = int(num_str)
# print(num_int)  # Output: 123
# print(type(num_int))


# # Converting int to string
# num_int = 123
# num_str = str(num_int)
# print(num_str)  # Output: "123"

# # Converting float to string
# num_float = 123.45
# num_str = str(num_float)
# print(num_str)  # Output: "123.45"

# #Converting boolean to String
# num_bool=False;
# num_str = str(num_bool);
# print(num_str);
# print(type(num_str))
# print(num_str.lower())

#Converting tuple into list
# tuple_val = (2,5,7);
# list_val = list(tuple_val);
# print(list_val)
# print(list_val[1]);

#Converting list into tuple
# list_val= [2,5,7];
# tuple_val = tuple(list_val);
# print(tuple_val)
# print(tuple_val[2]);


# list_of_tuples = [(1,2),(4,8),(4,8)];
# dict_val= dict(list_of_tuples); #dictonaries
# print(dict_val)


# first Question

num1= int(input("Enter Any Number "));
num2= int(input("Enter Any Number "));

print("Addition ",num1 + num2);


side = int(input("Enter the side of Square "))
area=side * side;
print(area);

if(num1 >= num2):
    print("True");
else:
     print("False")