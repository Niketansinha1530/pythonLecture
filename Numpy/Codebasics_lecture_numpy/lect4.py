import numpy as np

# Data Types in NumPy Arrays

var1 = np.array([1,2,3,4])
print("Data type: ",var1.dtype) #int64

var2 = np.array([1.1,2.1,3.1,4.1])
print("Data type: ",var2.dtype) #float64

var3 = np.array(["A","B","C","D"])
print("Data type: ",var3.dtype) #U1
print("***************************************")

# Convert Data types

x = np.array([1,2,3,4],dtype=np.int8)
print("Data type: ",x.dtype)
print(x)


x1 = np.array([1,2,3,4],dtype=np.float16)
print("Data type: ",x1.dtype)
print(x1)

x2 = np.array([1,2,0,4],dtype=np.bool_)
print("Data type: ",x2.dtype)
print(x2)


print("***************************************")
# Convert by using function

y = np.array([1,2,3,4])
print("Data type: ",y.dtype)
print(y)

newY = np.float32(y)
print("Data type: ",newY.dtype)
print(newY)

#Astype function

z = np.array([1,2,3,4,5])
new_z=  z.astype(complex) #[1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]

print(z)
print(new_z)