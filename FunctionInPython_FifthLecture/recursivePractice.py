# print sum of n natural number

def calSum(n):
    if(n==1):
     return 1
    else:
      return  n + calSum(n-1)
    
# print("hello")
print(calSum(50))

# cricketer = ["Virat Kohli","Rohit Sharma","Rishab pant","Sachin","rahul"]
# # print(len(cricketer))
# lenghtOfList = len(cricketer)

# def printCricketer(n=0):

#     if(n==lenghtOfList):
#         return
#     else:
#         print(cricketer[n])
#         printCricketer(n+1)

# printCricketer()
    
