student_scores=input("Enter the list of student score\n").split()
for n in range(0,len(student_scores)) :
    student_scores[n]=int(student_scores[n])
print(student_scores)
maxi=student_scores[0]
for n in student_scores :
    if maxi<n :
        maxi=n
print(f"The highest score in the class is {maxi}\n")
mini=student_scores[0]
for n in student_scores :
    if mini>n :
        mini=n
print(f"The Lowest score in the class is {mini}")
     
    
