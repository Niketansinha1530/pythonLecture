

# set is the collection of the unordered items.
# Each elements in the set must be unique & immutable.
# sets are mutuable but elements are immutable
# we do not add lists and dictionary in set because these are mutable

# setsValue={"ram","Lakshman","sita","sita"}
# print(setsValue)

# # Null set
# null_set = set()
# null_set.add("yodha")
# print(null_set)
# print(type(null_set))

# collection ={451,2,(3,4,5)}
# collection.add("Radha")
# collection.remove(451)
# print(collection)
# collection.clear() # remove all element from the set
# print(collection)

# cars = {"BMW","Volvo","Suzuqi"}

# print(cars)
# print(cars.pop()) # Remove random value from set

tup= (1,2,3,[1,2,3])
print(tup)
# tup[2]=5 # TypeError: 'tuple' object does not support item assignment
newList=list(tup[3])
print(newList)
print(type(tup))
print(newList[0])