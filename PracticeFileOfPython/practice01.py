# Q1. 

# poem_list =[
#     "Twinkle, twinkle, little star,","How I wonder what you are!",
#     "Up above the world so high,","Like a diamond in the sky.","\n"
#     "Then the traveler in the dark","Thanks you for your tiny spark;",
#     "He could not see which way to go,","If you did not twinkle so.","\n"
#     "Though I know not what you are","Twinkle, twinkle, little star.",
#     "Twinkle, twinkle, little star,","How I wonder what you are!", "\n"
#     "When the blazing sun is gone,","When he nothing shines upon,",
#     "Then you show your little light,","Twinkle, twinkle, all the night.",
# ]

# for i in poem_list:
#     print(i)

# Q2.
# import nltk 
# from nltk.corpus import gutenberg
# # nltk.download('gutenberg') # download the gutenberg dataset
# print("here is the the list",gutenberg.fileids()) # print the fileids in the gutenberg dataset

# poem_text = gutenberg.raw('austen-sense.txt') # get the raw text of the blake-poems.txt file
# print(poem_text[:500]) # print the raw text of the blake-poems.txt file

# Q3.

# for i in range(1,11):
#     print("5"," X ",i, " = ",5*i)

# Q4.
# import os

# folder_path = r"D:\Python\Oops"
# files = os.listdir(folder_path)


# print("files and folder in:",folder_path)
# count = 1
# for file in files:
#     print(f"{count}.",file)
#     count = count + 1
# print("Data type return by listdir",type(files))


# import os 

# folder_path = r"D:\Python\Oops\bank.py"
# info = os.stat(folder_path)
# print("File Size in Bytes is:",info.st_size)

# Q5.
import datetime
from pathlib import Path
folder = Path(r"D:\Python\Oops\bank.py")

last_modified = datetime.datetime.fromtimestamp(folder.stat().st_mtime)
last_accessed = datetime.datetime.fromtimestamp(folder.stat().st_atime)

print("Folder Name:", folder.name)
print("Parent Directory:", folder.parent)
print("Is Directory?", folder.is_dir())
print("Is File?", folder.is_file())
print("Size (bytes):", folder.stat().st_size)
print("Last Modified:", last_modified.strftime("%Y-%m-%d %H:%M:%S:%p"))
print("Last Accessed:",  last_accessed.strftime("%Y-%m-%d %H:%M:%S:%p"))
