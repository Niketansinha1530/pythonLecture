import numpy as np

#Special Types of Arrays (filled with specific value)

# 1. Create Numpy Array using  Numpy Functions


#-> Array filled with 0's
ar_Zero = np.zeros(4)

ar_Zero1 = np.zeros((2,3))
print(ar_Zero)
print()
print(ar_Zero1)
print("*************************************")
#-> Array filled with 1's
ar_ones = np.ones(4,dtype="i")

ar_ones1 = np.ones((2,3),dtype="i")
print(ar_ones)
print()
print(ar_ones1)
print("*************************************")
#-> Create an empty Array

emptyArray = np.empty((2,3))
print(emptyArray) #random value print
print("*************************************")

#-> An Array with a range of elements
ar_range = np.arange(4)
print(ar_range)
print("*************************************")
#-> Array diagonal element filled with 1's
ar_dia = np.eye(3,dtype="i")#Create 2-D Array and at diagonal place put 1
print(ar_dia) 
print("*************************************")
#-> Creatae an array with values that are spaced linearly in a specified interval

ar_lin = np.linspace(1,20,num=10,dtype="i")
print(ar_lin)