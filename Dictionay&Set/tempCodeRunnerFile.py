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
print(student["Marks"]["Additional"]["Hindi "])