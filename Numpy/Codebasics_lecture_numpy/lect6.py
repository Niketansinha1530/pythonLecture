import numpy as np

# Arithmetic Operation in Numpy Arrays


# a + b  -> np.add(a,b)
# a - b  -> np.subtract(a,b)
# a * b  -> np.multiply(a,b)
# a / b  -> np.divide(a,b)
# a % b  -> np.mod(a,b)
# a ** b  -> np.power(a,b)
# 1 / a  -> np.reciprocal(a)


# Addition

var1= np.array([1,2,3,4,5])
# new_var1 = var1 + 10
new_var1 = np.add(var1,10)

print("Addition: ",new_var1)

# Subtraction

var2 = np.array([1,2,3,4,5])
# new_var2 = var2 - 10
new_var2 = np.subtract(var2,10)

print("Subtraction: ",new_var2)

# mutliplcation

var3 = np.array([1,2,3,4,5])
# new_var3 = var3 * 10
new_var3 = np.multiply(var3,10)

print("Multiplication: ",new_var3)

# Divide

var4 = np.array([1,2,3,4,5])
# new_var4 = var4 / 10
new_var4 = np.divide(var4,10)

print("Division: ",new_var4)

# Power

var5 = np.array([1,2,3,4,5])
# new_var5 = var5 ** 2
new_var5 = np.power(var5,2)

print("Power: ",new_var5)

# Reciprocal

var6 = np.array([1,2,3,4,5])
# new_var6 = 1 / var6
new_var6 = np.reciprocal(var6)

print("Reciprocal: ",new_var6)

# Mode

var7 = np.array([1,2,3,4,5])
# new_var7 = var7 % 2
new_var7 = np.mod(var7,2)

print("Mode: ",new_var7)
print("*********************************************************")
# same operation we can perform with 2 array we can perform all arithmetic operation with 2 arrays
 

# num1 = np.array([1,2,3,4,5])
# num2 = np.array([1,2,3,4,5])
# print("Num1 : ",num1)
# print("Num2 : ",num2)
# print(num1 ** num2)

# same operation we can perform with 2D array we can perform all arithmetic operation with 2D arrays

num1 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
num2 = np.array([[10,20,30,40,50],[10,20,30,40,50]])
print(num1)
print()
print(num2)
print()
print(num1 + num2)