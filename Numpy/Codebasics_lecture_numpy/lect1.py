import sys
import numpy as np



# List V/s Numpy Array
# numList = [1,2,3,4]
# print("List: ",numList)


# array= np.array([1,2,3,4])
# print("Array : ",array)
# print("Dimension of Array:",array.ndim)

listNum = []

for i in range(1,6):
    int_i= int(input("Enter Number: "))
    listNum.append(int_i)

listToArray = np.array(listNum)
print(listToArray)
print("***************************************************")
ar1 = np.array([1,2,3,4])
ar2 = np.array([[1,2,3,4],[1,2,3,4]])
ar3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])


print(ar1)
print("ar1 dimension: ",ar1.ndim)
print("******************************")
print(ar2)
print("ar2 dimension: ",ar2.ndim)
print("******************************")
print(ar3)
print("ar3 dimension: ",ar3.ndim)

newAR= np.array([1,2,3],ndmin=3)
print(newAR)
print(newAR.ndim)