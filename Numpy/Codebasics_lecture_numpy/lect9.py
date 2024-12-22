import numpy as np

# Indexing & Slicing in NumPy Arrays.

#INDEXING

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
arr3 = np.array([[[41,42,43,44],[11,21,31,41],[12,22,32,42]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])


print("Index of 1d array : ",arr1[0]) #1
print("Index of 2d array : ",arr2[0,1]) #12
print("Index of 3d array : ",arr3[0,1,1]) #21

# SLICING
print("Slicing: ***************************************************")
var = np.array([11,21,23,12,33,43,44,55,66,77])
        
# Slicing in 1 D Array
print(var[1:]) #From index 1 to end
print(var[3:8]) #From index 3 to index 8
print(var[0:10:2]) # start: end : step

# Slicing in 2 D Array

print(arr2[2,1:])
print(arr2[0, 0:])

# Slicing in 3 D Array

print(arr3[1,2, 0:])
print(arr3[0,0, 0:])

print(arr3[0,1,3])