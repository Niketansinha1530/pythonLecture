import numpy as np

# NumPy Array Function (Insert and Delete Function)

num_ar = np.array([1,2,3,4])
print(num_ar)
# print(type(num_ar))
# print(num_ar.dtype) 

v= np.insert(num_ar,3,20)
# v = np.insert(num_ar,(2,4),[23,33]) # Array_Name,Index, Value

print(num_ar) # not change
print("New Value inserted",v)

# append() function

newAppendArray = np.append(num_ar,6)
print("Append element: ",newAppendArray)

print("*************************************")

# we can also insert value in 2d array

#insert in 2d array
num_2 = np.array([[1,2,3,4],[5,3,2,4]])
print(num_2)

# newNum2 = np.insert(num_2,1,12,axis=1)
# newNum2 = np.append(num_2,[[12],[13]],axis=1)
newNum2 = np.append(num_2,[[12,11,13,14]],axis=0)
print(newNum2)


print("************** Delete *****************")

num_ar2 = np.array([11,12,13,14])
de = np.delete(num_ar2,0)
print(de)