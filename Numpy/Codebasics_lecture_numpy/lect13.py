import numpy as np

# NumPy Arrays Functions (Search, Sort, Search Sorted, Filter)

# Search Array: Search an array for a certain value, and return the indexes that get a match.

# Searching
print("************ Searching *************")
num1 = np.array([1,2,3,4,2,1,5,5,6])

index = np.where( num1 ==2)

print("Index : ",index)
print(type(index)) # np.where() return a tuple.
print("********************************************")
# Search Sorted Array: Which perform a binary search in the array, and return the index where the speicified value would be inserted to maintain the searach order.

num = np.array([11,12,14,15,16])

index = np.searchsorted( num,[13,17],side="left") # 13 number where we placed # we can also provide from where you want to search from left side or right side.

print("At place  : ",index)

# Sort Array

var = np.array([22,31,42,3,1,2,3,8,3,83,2])

var_sort = np.sort(var)

print("Sorted Array: ",var_sort)


var_aplha= np.array(['a','e','b','d','c'])

print(np.sort( var_aplha))

# 2d sorted array

var_2 = np.array([[22,31,42,3],[1,2,3,8],[3,83,2,1]])

print(np.sort(var_2)) # sort every row.


# Filter Array : Getting some elements out of an existing array and creating a new array out of them.

print("********** Filter ************")

# var_3 = np.array(['a','s','d','g'])

# f=[True,False,True,False]

# new_a = var_3[f]

# print(new_a)
# print(type(new_a))

var4 = np.array([2,3,5,4,6,7,12])

new_ar = np.where( var4%2==0) # return index

filter_ar = var4[new_ar]
print(new_ar)
print(filter_ar)
