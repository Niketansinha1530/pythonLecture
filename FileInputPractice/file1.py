#READ MODE

# f = open(r"D:\Python\FileInputPractice\demo.txt","r")
# data= f.read()
# print(data)
# f.close()

# f=open(r"D:\Python\FileInputPractice\demo.txt","r")
# data=f.read(6)
# print(data)
# print(type(data))
# f.close()

# with open(r"D:\Python\FileInputPractice\demo.txt","r") as f:
#     Line1=f.readline()
#     print(Line1)
#     Line2=f.readlines() #It return a list of lines
#     print(Line2)

# print(type(Line2))
# print(len(Line2))
# print(Line2[1])


# with open(r"D:\Python\FileInputPractice\demo.txt","r") as f:
#     data = f.readlines()
#     print(type(data))
#     print(len(data))


# f = open(r"D:\Python\FileInputPractice\demo.txt", "r")
# for x in f:
#   print(x)


#WRITE MODE

with open(r"D:\Python\FileInputPractice\demo.txt","w") as f:
    data=f.write("Hello Everyone") #It return the number of characters written
    print(data)

#append mode
with open(r"D:\Python\FileInputPractice\demo.txt","a") as f:
    data_append=f.write("\t this line add after Hello everyone") #It return the number of characters written

with open(r"D:\Python\FileInputPractice\demo.txt","r") as f:
    data1=f.read()
    print(data1)