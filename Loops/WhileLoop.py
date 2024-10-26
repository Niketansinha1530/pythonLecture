# # While Loop
# count =1
# while(count<=5):
#     print("hello")
#     count +=1

# print(count)

#q1 print Numbers from 1 to 100

# i = 1

# while(i<=100):
#     print(i)
#     i += 1

#q1 print Numbers from 100 to 1

# i = 100
# while(i>=1):
#     print(i)
#     i -= 1

# Q3 print the multiplication table of a number n

# num = int(input("Enter any number: "))

# i =1

# while(i<=10):
#     print(num," X ",i, " = ", i*num)
#     i +=1

# Q4 print the elements of the following list using a loop

# i = 1
# while(i<=10):
#     print(i*i)
#     i +=1

# Q5 search for a number x in this tuple using loop

# sq_tup = (1,4,9,16,25,36,49,64,81,100)
# numX = int(input("Enter a number you want to find: "))
# length = len(sq_tup)
# i=0
# while(i<=length-1):
#     if(numX == sq_tup[i]):
#         print("Number find at index",i)
#         break
#     else:
#         if(i==length-1):
#             print("numX not found in the given tuple")
    
#     i += 1



# Q6 print

sq_list = [1,4,9,16,25,36,49,64,81,100]

list_lenght = len(sq_list)
i = 0
while(i<=list_lenght-1):
    print(sq_list[i])
    i += 1 