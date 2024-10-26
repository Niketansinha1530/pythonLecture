# fruitList=["Apple","Banana","Gauva","Pineapple","BlackBerry"];
# # Create a list of your five favorite fruits and print them.
# print(fruitList)

# # Replace the second fruit in the list with a new fruit and print the updated list.

# fruitList.pop(1)
# fruitList.insert(1,"Orange")
# print(fruitList)

# # Add two more fruits to the end of the list.

# fruitList.append("Papaya")
# fruitList.append("Strawberry")
# print(fruitList)

# # Remove the first fruit from the list.

# fruitList.remove("Apple")
# print(fruitList)

# # Print the last fruit in the list without removing it.
# # Find the total number of fruits in the list.
# LenghtOfFruitList = len(fruitList)
# print(fruitList[LenghtOfFruitList-1])
# print(fruitList)

# ******************************* Second Question   *****************************************
marksList = [12,15,12,14,19]
# print(marksList)
# marksList.reverse()
# newList=marksList.copy()
# print(newList)

reversedList=list(reversed(marksList))
print(reversedList)