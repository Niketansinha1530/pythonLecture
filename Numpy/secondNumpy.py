# First class through W3Shool

import numpy as np

# NumPy is usually imported under the np alias.
# arr1= np.array([1,2,3,4,5])
# arr2 = np.array([1,2,3,4,5])

# print(arr1 + arr2)

# print(np.__version__) #2.1.3

# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

# marks = np.array([20,18,17,20,15])

# print(marks)
# print(type(marks))
# print(len(marks))

# print("***************************")

#  To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

# marks_list=(1,2,3,4,5)

# newList =np.array(marks_list)
# print(type(newList))


arr_0d = np.array(3)
arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],[4,5,6]])

# print(arr_0d)
# print(arr_1d)
# print(arr_2d)


# print(arr_2d[1][1]) # index axising

# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

arr = np.array([[[1, 66, 3], [4, 5, 6]], [[1, 56, 3], [4, 5, 6]]])

# print(arr[1][0][1]) #index accessing
# print(arr[0][0][1]) #index accessing

arr3d = np.array([[[1,2,3],[2,3,4]],[[1,2,3],[2,3,4]]])
print(arr3d)