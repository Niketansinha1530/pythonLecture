Students = [
    ["Rohan",85],
    ["Aisha",92],
    ["Vikram",92],
    ["Priya",98],
    ["Ranjan",89],
]

marks_list=[]

for st in Students:
    marks_list.append(st[1])

print(marks_list)
marks_list.sort()
print(marks_list)

secondHighest= marks_list[len(marks_list)-2]
print("Second highest marks: ",secondHighest)

for st in Students:
    if secondHighest==st[1]:
        print(st[0])

