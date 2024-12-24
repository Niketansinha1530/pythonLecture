import numpy as np

# The Difference between copy and view

# Copy v/s View 
 
# Copy 

# 1. The copy owns the data.
# 2. The copy of an array is a new array.
# 3. The changes made in the copy data does not reflect in the original array

marks = np. array([12,13,14,15,16])
newMarks = marks.copy()


marks[1]=20

print("Copy Marks :",newMarks)
print("Original Marks: ",marks)

# View

# 1. The view does not own the data
# 2. A view of the original array.
# 3. Any changes made to the view will affect the original array, and any changes made to the original array will affect the view
print()
num = np. array([122,123,124,215,126])
newNum = num.view()

newNum[1]=43

print("View NewNum :",newNum)
print("Original Num: ",num)