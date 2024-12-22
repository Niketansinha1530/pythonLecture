import numpy as np

# Iterating Numpy Arrays

# Iteration on 1D Array
var = np.arange(1,11)
print(var)

for i in range(11):
    print(i,end = ",")

print()
# Iteration on 2 Array
var2 = np.arange(0,8).reshape(4,2)
print(var2)

for i in var2:
    for j in i:
     print(j)

print("************************")

# Iterate by Function

# nditer iterate value
for i in np.nditer(var2):
   print(i)



num2 = np.array([[11,22,33,44],[21,32,43,54]])

# ndenumerate also give index of array
for i,d in np.ndenumerate(num2):
   print(i,d)