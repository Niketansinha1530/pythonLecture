import numpy as np

#Shape & Reshaping in Numpy Arrays.

# Shape Function 

var = np.array([[1,2,3],[2,3,5]])
print(var)
print(var.shape) #(2, 3)

var1 = np.array([1,2,3,4],ndmin=2)
print(var1)
print(var1.shape)

# Reshape Function
print("Reshape Function in 2D")

x = np.array([1,2,3,4,5,6])
print(x)
print("Dimension of X",x.ndim)
print("*******************************")
newX = x.reshape((3,2)) # convert one Dimension to 2 Dimension
print(newX)
print("Dimension of newX: ",newX.ndim)

print("***************************************************")

print("Reshape Function in 3D")

y = np.array([1,2,3,4,5,6,7,8,9,1,2,3])
print(x)
print("Dimension of y",y.ndim)
print("*******************************")
newY = y.reshape((3,2,2)) # convert one Dimension to 2-Dimension 2 row and 2 column of 3 matrix
print(newY)
print("Dimension of newY: ",newY.ndim)

print("***************************************************")

print("Reshape Function in 1D")
newZ = newY.reshape(-1) # convert into 1 dimension
print(newZ)
print("Dimension of newY: ",newZ.ndim)


# shape function
# num = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

# print(num.shape) #(2, 2, 3)

# Reshape Function
print("Reshape Function")
num = np.array([1,2,3,4,5,6,1,2])
newNum = num.reshape((2,2,2))
print(newNum)
print(newNum.ndim)

new_1 = newNum.reshape(-1)
print(new_1)