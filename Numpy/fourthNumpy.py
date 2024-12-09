# Learning slicing

# Slicing Arrays
"""Slicing in python means taking elements from one given index to another given index.

1. We pass slice instead of index like this: [start:end].

2. We can also define the step, like this: [start:end:step].

3. If we don't pass start its considered 0

4. If we don't pass end its considered length of array in that dimension

5. If we don't pass step its considered 1"""

import numpy as np

arr = np.array([1,2,3,4,6,7,8,4,6])

# print(arr[1:3]) #The result includes the start index, but excludes the end index.

# print(arr[3:]) #Slice elements from index 3 to the end of the array:


# print(arr[:4])  # Slice elements from the beginning to index 4 (not included):

# print(arr[:len(arr)]) 

"""Negative Slicing"""

arr1= np.array([10, 12, 33,54, 115, 36, 57])

# print(arr1[-3:-1]) #The result includes the start index, but excludes the end index.

# print(arr1[0:7:3])

"""Step slicing in Python, particularly when using the NumPy library, refers to selecting elements from an array at a regular interval or "step." This is controlled by the third parameter in the slicing syntax"""

""" array[start:stop:step] """

tabArray = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# print(tabArray[0:len(tabArray):3]) # every third element will be pring

# print(tabArray[::-1]) #reverse the array

# print(tabArray[::2]) #print after second element

# print(tabArray[::1]) # print after first element


"""Slicing 2-D Arrays"""

mat = np.array([[11,24,3,4,5,6],[26,4,5,6,7,8]])

print(mat[1, 0:3] ) #From the second row, slice elements from index 1 to index 3 (not included):

print(mat[0:2 ,1]) #From all row, return index 1

print(mat[0:2 , 0:3]) #From both elements, slice index 1 to index 4 (not included), this will return a 2-D array


