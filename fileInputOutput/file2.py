#  'r+' read plus overwrite (pointer start from beginning) - no truncate
#  'w+' write plus overwrite  - trucate the previous content
#  'a+' append plus append the data from the last and -no truncate

# read plus  --------------

# f= open("demo.txt","r+")
# f.write(" How are you")
# f.close()

# append Plus  ----------------

# f= open("demo.txt","a+")
# f.write("\t How are you")
# f.close()

# write Plus   ------------------

# f= open("demo.txt","w+")
# f.write("\t How are you")
# f.close()

# with Syntax

with open("demo.txt","r") as f:
    data=f.read()
    print(data) # here we do not need to close

with open("demo.txt","w") as f:
    f.write("New data add")