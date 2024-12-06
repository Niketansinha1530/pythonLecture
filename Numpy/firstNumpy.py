import numpy as np
import sys

#List
# numList=[2,4,5,5]
# print(numList)


# 3main benefits of numpy array over a python list,
# 1. Less Memory
# 2. Fast
# 3. Convinient

ar = np.array([3,4,5,6,7])

print(ar[0])
print(ar[1])

l = range(1000)
name="niketan"
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)

#lists multiplication
a1_list = [1,2,3,4,5]
a2_list = [5,5,5,5]

result = [(x*y) for x,y in zip(a1_list,a2_list)]
print(result)

# array multiplication
# a1 = np.array([1,2,3,4,5])
# a2 = np.array([5,5,5,5,5])

# result = a1*a2
# print(result)

print("******************************************")
digits = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [6, 7, 9],
    ])

print(digits+2)

# https://www.w3schools.com/python/numpy/numpy_getting_started.asp