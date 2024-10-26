# str = input("Enter your name: ");
# nameLength = len(str);
# print("No of character in your name is : ",nameLength);

#  ---------------------------------------------------------  Concatination -------------------------------------------------- #

# str = "Hierank "
# str2 = "Business "
# str3 = "School"
# collegeName= str + str2 + str3;

# print("My college Name is : ",collegeName , len(collegeName))

#  ---------------------------------------------------------  Concatination -------------------------------------------------- #

#  ---------------------------------------------------------  Index Accessing -------------------------------------------------- #


# print(collegeName[0])
# print(collegeName[1])
# print(collegeName[2])
# print(collegeName[3])
# print(collegeName[4])
# print(collegeName[5])
# print(collegeName[6])
# print(collegeName[7])
# collegeName[7]= "B"
# print(collegeName[7]) #str' object does not support item assignment

#  ---------------------------------------------------------  Index Accessing -------------------------------------------------- #

#  ---------------------------------------------------------  Slicing  -------------------------------------------------- #

# str = "HierankBusinessSchool"

# print(str[0:]); # HierankBusinessSchool
# print(str[:len(str)]); # HierankBusinessSchool
# print(str[0:7]) # Hierank

#  ---------------------------------------------------------  Slicing  -------------------------------------------------- #

#  ---------------------------------------------------------  Negative Indexing   -------------------------------------------------- #
#    A  P  P  L  E
#    -5 -4 -3 -2 -1

# str = "apple" 
# print(str[-5:-2]) # app
# print(str[-5:]) # apple
# print(str[:-1]) # appl

#  ---------------------------------------------------------  Negative Indexing   -------------------------------------------------- #


#  ---------------------------------------------------------  String Function  -------------------------------------------------- #

#Notes

# str.endsWith(“er.“) #returns true if string ends with substr
# str = “I am a coder.”
# str.count(“am“) #counts the occurrence of substr in string
# str.capitalize( ) #capitalizes 1st char
# str.find( word ) #returns 1st index of 1st occurrence
# str.replace( old, new ) #replaces all occurrences of old with new

# str = "I am a Coder."

# # flag = str.endswith("er."); #True
# flag = str.endswith("ER."); #False
# print(flag)


sentence = "every day, every night, in every way, I am getting better and better."
print(sentence.count("every"))

print(sentence.capitalize())

print(sentence.find("getting"))
print(len(sentence));

print(sentence[43])
print(sentence)

newstr = sentence.capitalize()
print(newstr)

newSentence = sentence.replace("every","yesterday")
print(newSentence)

# ****************************************  Repetition *****************************************

# s ="lala"
# print(s *3) # lalalalalala 