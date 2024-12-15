import numpy as np
# Creating Random Valued Arrays

# Create Numpy Arrays with Random Numbers


#Rand() Function
# -> rand() : The function is used to generate a random value between 0 to 1.

randomArray = np.random.rand(2)
# randomArray = np.random.rand(2,2) #2D Array with random elements
print(randomArray)
print("********************************")
# -> randn() : The function is used to generate a random value close to zero. This may return positive or negative numbers as well.
randNearToZero = np.random.randn(2)
print(randNearToZero)
print("********************************")
# -> ranf()  : The function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0) 1 is not included

x = np.random.ranf(2)
print(x)
print("********************************")
# -> randint() : the function is used to generate a random number be in a given range.
y = np.random.randint(1,40,5) #randint(min,max,totalNumber)
print(y)