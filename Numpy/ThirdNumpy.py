import numpy as np

# a = np.array(23)
# b = np.array([1,2,3])
# c = np.array([[1,2,3],[10,20,30]])
# d = np.array([[[1,2,3],[10,20,30]],[[1,2,3],[10,20,30]]])

# # NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# e = np.array([1,2,4,5],ndmin=5)

# print(e.ndim)

# Array Indexing

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[10,20,30]])
arr3 = np.array([[[1,2,3],[13,23,32]],[[11,22,33],[41,42,43]]])

print("3 element of array: ",arr1[2])
print("First row ka 2nd element: ",arr2[0][1])
print("second row ka last element: ",arr2[1][2])
print("Same way of accessing: ", arr2[1,1]) # Different way of accessing


print(arr3[0,1,2]) #32

print(arr3[1,1,1]) #index accesing in 3d array

print(arr2[0,-1]) #negative index

print(arr3[1,1,-1])