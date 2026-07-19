marks=[]
with open("marks.txt","r") as f1: # context manager is used here
    marks=[int(line.strip()) for line in f1] # pythonic way of writing code using comprehension

students=[]
with open("names.txt","r") as f2:
    students=[line.strip() for line in f2]

for index,(s,n) in enumerate(zip(students,marks)):
    print(f"{index} ) {s} : {n}")

total = sum(marks)
avg = sum(marks)/len(marks)

print(f"The average mark of the class is {avg}")
print(f"The total mark of the class is {total}")
