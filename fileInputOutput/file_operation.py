# f = open("demo.txt", "r")  # "r" opens the file in read mode
# # data = f.read(21) # we can pass int value that's print no of character in file
# data = f.read(21)
# print(data)
# # print(type(data))
# f.close()


# # 'r'  Open for reading (default)
# # 'w'  Open for writing, truncating the file first (remove previous data)
# # 'x'  Create a new file and open it for writing
# # 'a'  Open for writing, appending to the end of the file if it exits
# # 'b'  binary mode
# # 't'  text Mode (default)
# # '+'  Open a disk file for updating(reading and writing)

# read mode

f=open("demo2.txt","r")


line1=f.readline()
print(line1)

line2=f.readline()
print(line2)

line3=f.readline()
print(line3) # if content is not their then print next white line

# print("helo")
# data= f.read()

# print(data)

f.close()


#write mode
# f = open("demo2.txt","w")

# f.write("India loose")

# f.close()

# append mode
# f = open("demo2.txt","a")

# f.write("India loose")

# f.close()