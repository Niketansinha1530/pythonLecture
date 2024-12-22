import numpy as np

# Broadcasting NumPy Arrays

# Rules to avoiding broadcasting Error
# 1. Need to be same dimension
# 2. Need to row ya column may se koi 1 ho na chaiya

#IMPORTANT CONCEPT

# var1 = np.array([1,2,3,4])
# print(var1)
# var2 = np.array([1,2,3])
# print(var2)

# print("Sum: ", var1 + var2) #ValueError: operands could not be broadcast together with shapes (4,) (3,)
print("****************************************")
varX1 = np.array([[1,2,3]]) # One row three column(1,3)
print("Shape : ",np.shape(varX1))
print(varX1)
print()


varX2 = np.array([[1],[2],[3]]) #  Three rows one column(3,1)
print("Shape : ",np.shape(varX2))
print(varX2)


print()
varX3= varX1 + varX2
print("Shape: ",np.shape(varX3))
print(varX3)

print("***************************************")
varY1= np.array([[1],[2]]) #(2, 1)
print("Shape: ",np.shape(varY1))
print(varY1)
print()

varY2= np.array([[1,2,3],[2,3,4]]) #(2, 3)
print("Shape: ",np.shape(varY2))
print(varY2)
print()

varY3 = varY2 + varY1
print("Shape : ",np.shape(varY3))
print(varY3)

print("***************************************")

varZ1= np.array([[1,2],[-1,0]]) # (2,2)
print("Shape: ",np.shape(varZ1))
print(varZ1)
print()

varZ2= np.array([[3,2],[1,-2]]) # (2,2)
print("Shape: ",np.shape(varZ2))
print(varZ2)
print()

varZ3 = varZ2 + varZ1
print("Shape : ",np.shape(varZ3))
print(varZ3)