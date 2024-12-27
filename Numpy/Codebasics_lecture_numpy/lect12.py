import numpy as np

# Join & Split Function Numpy Arrays

#Join Array: Joining means putting contents of two or more arrays in a single array.

# for Joining its required to if we join other array it should be same shape other wise joining not perform.(2D Array)

var = np.array([1,2,3,4,5])
var1 = np.array([6,7,8,9,7])

ar = np.concatenate((var,var1))

print("Joined Array ", ar)

# In 2D array joining will perform along axis

num = np.array([[1,2,3,4],[1,2,3,4]])
num1 = np.array([[5,6,7,8],[5,6,7,8]])

newNum = np.concatenate((num,num1),axis =1) # by default join 2d array column axis
# axis =0 means column
# axis = 1 means row
print("Joined 2D array : ")
print(newNum)

print("************************************************")
# we can also use stake function to join array

num_ar1 = np.array([1,2,3,4,5])
num_ar2 = np.array([6,7,8,9,7])

# total_ar = np.stack((var,var1),axis=1) # it take as a 2d Array
# we have total three stake function if you don't use axis attribute.
# np.hstack() # row along
# np.vstack() # column along
# np.dstack() # Height along


# total_ar = np.hstack((num_ar1,num_ar2)) #[1 2 3 4 5 6 7 8 9 7]

# total_ar = np.vstack((num_ar1,num_ar2))  #[[1 2 3 4 5]
                                          #  [6 7 8 9 7]]

total_ar = np.dstack((num_ar1,num_ar2))

"""
[[[1 6]
  [2 7]
  [3 8]
  [4 9]
  [5 7]]]
"""
print("Joined Array ")
print(total_ar)



# Split Array : Splitting breaks one array into multiple



print("**************************************")
print("Split Array")

marks = np.array([1,2,3,4,5,6])

print(marks)
new_marks = np.split(marks,2) # no of split you want
print()
print(new_marks)
print("Type : ",type(new_marks)) # List
# print(new_marks[0][2])
print(new_marks[0])
print(" Split in 2D *****************************") # split in 2d
matrix = np.array([[1,2,3,4,5,6],[7,8,9,6,1,2]])
print(matrix)


new_mat = np.split(matrix,2)

new_mat2 = np.split(matrix,3,axis=1) #row

print(new_mat)
print(type(new_mat)) # list
print(new_mat[1][0][1])


print("new matrix: ",new_mat[0])
print()


print("Axis along matrix split")
print(new_mat2)
print(new_mat2[0])