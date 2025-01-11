import numpy as np

py_list = [1,2,3,4,"Honey",3.3, False]
print(type(py_list))
print("List: ",py_list)

print("***************************************")

py_array =np.array([1,2,3,4,5])
print(type(py_array))
print("NumPy Array:",py_array)

print("Shape of Array: ",py_array.shape)
print("Size of Array: ",py_array.size)
print("Type of Array: ",py_array.dtype)

print("*****************************")

ar_zeroes = np.zeros((2,3))

print(ar_zeroes)
print(ar_zeroes.dtype)

ar_ones = np.ones((3,2))
print(ar_ones)

ar_range = np.arange(1,14,2)
print("arange Function: ",ar_range)

ar_linspace = np.linspace(0,0.9,7)
print("Linespace Function: ",ar_linspace)

print("*******************************")

ar1 = np.array([1,2,3,4,5])
print(ar1)
print("Dimension of ar1 ",ar1.ndim)


ar2 = np.array([[1,2,3,4],[2,3,4,5]])
print(ar2)
print("Dimension of ar2 ",ar2.ndim)

ar3 = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(ar3)
print("Dimension of ar3 ",ar3.ndim)

print("******************* Astype Function ************************")

# arr = np.array([1.5, 2.5, 3.5])
# try:
#     safe_arr = arr.astype(int , casting='safe')  # Prevent unsafe casting
# except TypeError as e:
#     print(e)  # Output: Cannot cast safely


arr = np.array([1.2, 3.4, 5.6])
int_arr = arr.astype(int, copy=False)
print(int_arr is arr)  # Output: False (usually a copy is created)
print(int_arr)
print(arr)
