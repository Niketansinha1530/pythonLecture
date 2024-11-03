
# with open("programming.txt","w") as f:
#     f.write("Hi Everyone \n")
#     f.write("We are learning File I/O \n")
#     f.write("using Python\n")
#     f.write("I like programming in Python")


# f = open("programming.txt","r")
# data=f.read()
# newData=data.replace("Python","Java")
# print(newData)

# f = open("programming.txt","w")
# f.write(newData)

# f = open("programming.txt","r")
# data=f.read()
# num=data.find("using")

# print(num)
# if(num==-1):
#     print("Not present")
# else:
#     print("present")

# def check_word_InLine():
#  word = "Java"
#  data=True #next line empty means false
#  line_no=1
#  with open("programming.txt","r") as f:
#     while data:
#         data=f.readline()
#         if(word in data):
#             print(line_no)
#             return
#         line_no +=1

#  return -1

# print(check_word_InLine())

# how many numbers are even in file

# listNumber = []

# with open("numbers.txt","r") as f:
#     data=f.read()
#     print(data)
    
#     num = ""
#     for i in range(len(data)):
#         if(data[i]==","):
#             IntNum =int(num)
#             listNumber.append(IntNum)
#             print(num)
#             num=""
#         else:
#             num += data[i]

# # print("Hello")
# print(listNumber)

# # print(type(listNumber))

# noOfEven=0

# for el in range(len(listNumber)):
#     if(el%2==0):
#         noOfEven +=1
    
# print(f"Total no of even in list is {noOfEven}")

# Second way
count =0
with open("numbers.txt","r") as f:
    data=f.read()
    print(data)

    nums= data.split(",")
    # print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1

print(f"No of even {count}")