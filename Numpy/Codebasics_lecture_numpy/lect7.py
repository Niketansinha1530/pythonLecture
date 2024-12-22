import numpy as np

# More Function in Arithmetic operation
# np.min(x)
# np.max(x)
# np.argmin(x)
# np.sqrt(x)
# np.sin(x)
# np.cos(x)
# np.cumsum(x)



var1 = np.array([22,32,45,32,55,12,46])

print("Minimum: ",np.min(var1))
print("Index of minimum value:",np.argmin(var1))
print()
print("Maximum: ",np.max(var1))
print("Index of maximum value:",np.argmax(var1))

print("*******************************************")

var2 = np.array([[21,22,3,44],[2,46,75,76]])
print("Minimum along column " ,np.min(var2,axis=0))
print("Minimum along row " ,np.min(var2,axis=1))
print("Minimum in whole 2d array " ,np.min(var2))