import numpy as np

# Important function in NumPy 
# Shuffle, Unique, Resize, Flatten, Ravel

# Shuffle

var = np.array([1,2,3,4,5,6])
np.random.shuffle(var)

print("Shuffle Array: ",var)
print("*****************Shuffle********************")
# Unique

var1 = np.array([1,2,4,5,6,6,1,3,2,2,3,4,5])

x = np.unique(var1,return_index=True,return_counts=True)

print("Unique Elemen: ",x)

print("*****************Unique********************")
# Resize

var3 = np.array([1,2,3,4,5,6])
y = np.resize(var3,(2,3))

print(y)

print("***************** Resize *******************")

print("Ravel : ",y.ravel(order="C")) ## convert 2d array into 1d array
print("Flatten : ",y.flatten(order = "F")) # convert 2d array into 1d array
