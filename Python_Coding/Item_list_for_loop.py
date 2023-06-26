#programming using for loop python
students_height=input("Input a list of students height\n").split()
for n in range(0,len(students_height)) :
    students_height[n]=int(students_height[n])
print(students_height)
s=0
for i in students_height:
                s+=i
print(s)
count=0
for i in students_height :
    count+=1
average = s/(count)
print(average)
