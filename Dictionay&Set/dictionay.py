# Disctionaries are used to store data values in Key:Value pairs
# They are unorder, Mutable(changeable) & don't allow duplicate keys
# **************** Basics of Dicitionary *************

# student = {
#     "name" : "Niketan",
#     "Roll_No" : 21,
#     "Age" : 21
# }

# print(student)

# print("\n")

# # we can make key generaly primitive datatype
# CourseInfo = {
#     "Name" : "Python Course",
#     "Tutor_Name" : "Shradha Khapra",
#     "NumberOfLecture" : 9,
#     "is_Adult":True,
#     "Topics" : ["Set","Dicitionay","tuple","List"],
#     (2,3,4) : "Niketan" , # it also work but not for list
#     #  [1,2,3] : "Halwa" #TypeError: unhashable type: 'list'
#     3+2j : "Hello"
# }

# print(CourseInfo)
# print(type(CourseInfo))

# print(CourseInfo["Topics"])
# print(CourseInfo[(2,3,4)])

# CourseInfo["student_Name"]="Niketan" #add new key value pair 
# CourseInfo[(2,3,4)]="Krishna" # overwrite value
# print(CourseInfo)

# **********  Creating a null Dicitionary ***************
# null_Dic = {}
# null_Dic["name"]="Niketan"
# null_Dic["surname"]="sinha"
# null_Dic["age"]=21


# print(type(null_Dic))
# print(null_Dic)


# ************* Nested Dicitionary ****************

student = {
    "Name" : "Niketan",
    "Surname" : "Sinha",
    "Marks" : {
        "Physics" : 98,
        "chemistry" : 94,
        "Math" : 92,
        "Additional" :{
            "Hindi" : 87,
            "PhysicalEducation":45
        }
    }
}

print(student["Name"])
print(student["Marks"])
print(student["Marks"]["Math"])
print(student["Marks"]["Additional"]["Hindi"])


# ************* Methods in Dict *************************

# myDict.keys( ) #returns all keys
# myDict.items( ) #returns all (key, val) pairs as tuples
# myDict.update( newDict ) #inserts the specified items to the dictionary
# myDict.values( ) #returns all values
# myDict.get( “key““ ) #re


# student = {
#     "Name" : "Niketan",
#     "Surname" : "Sinha",
#     "Marks" : {
#         "Physics" : 98,
#         "chemistry" : 94,
#         "Math" : 92,
#         "Additional" :{
#             "Hindi" : 87,
#             "PhysicalEducation":45
#         }
#     }
# }
# Converting dict into lists
# Student_List = list(student.keys())
# print(Student_List[0])


# print(student.keys()) # return all keys
# print(student.values()) # return all values

# print(student.items())
# listInfo=list(student.items())

# print(listInfo[2])


# student = {
#     "Name" : "Niketan",
#     "Surname" : "Sinha",
#     "Marks" : {
#         "Physics" : 98,
#         "chemistry" : 94
#     }
# }
# print(student)

# print(student["Surnam2"]) #KeyError: 'Surnam2' this is problemetisome time so prefer method

# print(student.get("Name"))
# print(student.get("Surname2")) # None NO error throw

# update_dict = {
#     "age" : 21,
#     "course":"BCA"
# }
# student.update(update_dict)

# print(student)

# print(student.keys())