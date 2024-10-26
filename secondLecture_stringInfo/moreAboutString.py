# 1. Immutable
# Once a string is created, it cannot be changed. You can't modify individual characters of a string. However, you can create a new string based on modifications.
# python
   
# s = "hello"
# s[0] = "H"  # This will raise an error because strings are immutable.

# ******************************2. Ordered (Indexable)*************************************

# 2. Ordered (Indexable)
# Strings are ordered sequences of characters, which means you can access characters by their position (index). Python uses zero-based indexing.
# python
   
# s = "hello"
# print(s[1])  # Output: "e"

# **************************************3. Support for Slicing********************************************************

# 3. Support for Slicing
# You can extract a portion of the string using slicing.
# python
   
# s = "hello"
# print(s[1:4])  # Output: "ell"

# ************************************4. String Concatenation**********************************************


# 4. String Concatenation
# Strings can be concatenated using the + operator.
# python
   
# s1 = "hello"
# s2 = " world"
# print(s1 + s2)  # Output: "hello world"

# ******************************************5. Repetition******************************************************


# 5. Repetition
# You can repeat strings using the * operator.
# python
   
# s = "ha"
# print(s * 3)  # Output: "hahaha"

# *********************************************6. Built-in Methods**********************************************


# 6. Built-in Methods
# Strings in Python come with many built-in methods, such as:
# upper(): Converts to uppercase.
# lower(): Converts to lowercase.
# strip(): Removes leading and trailing whitespace.
# replace(): Replaces parts of the string.
# split(): Splits the string into a list.
# join(): Joins elements of a list into a string.
# find(): Finds the index of a substring.
# python
   
# s = "hello world"
# print(s.upper())  # Output: "HELLO WORLD"

# ***********************************7. String Formatting************************************


# 7. String Formatting
# Python supports several ways to format strings:
# Using f-strings (since Python 3.6):
# python
   
# name = "Niketan"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
# Using format() method:
# python
   
# print("My name is {} and I am {} years old.".format(name, age))
# Using % operator:
# python
   
# print("My name is %s and I am %d years old." % (name, age))

# ****************************************8. Multiline Strings**************************************************


# 8. Multiline Strings
# You can create multiline strings using triple quotes (''' or """).
# python
   
# s = '''This is a
# multiline string.'''
# print(s)

# ************************************9. Escape Sequences**************************************************


# 9. Escape Sequences
# You can use backslashes to include special characters in strings, like \n (newline), \t (tab), \', \", and \\.
# python
   
# s = "This is a new line.\nAnd this is tab:\tHere"
# print(s)

# ************************************10. Unicode Support*********************************************************

# 10. Unicode Support
# Python strings are Unicode, which means they can store any character from any language (including emojis).
# python
   
# s = "こんにちは"  # Japanese for "Hello"
# print(s)

# ********************************11. Membership Operators******************************************************


# 11. Membership Operators
# You can use in and not in to check for the presence of a substring.
# python
   
# s = "hello"
# print("h" in s)  # Output: True
# print("z" not in s)  # Output: True

# *********************************** 12. Raw Strings  ********************************************************


# 12. Raw Strings
# Using an r before a string treats backslashes (\) as literal characters (used for regular expressions or file paths).
# python
   
# raw_str = r"C:\Users\Niketan"
# print(raw_str)  # Output: "C:\Users\Niketan"

# **********************************  13. Length Calculation   ****************************************************


# 13. Length Calculation
# The len() function gives the length of a string.
# python
   
# s = "hello"
# print(len(s))  # Output: 5

# *************************************************************************************************************************

