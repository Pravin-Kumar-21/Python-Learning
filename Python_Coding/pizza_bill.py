print("Welcome to Python Pizza Deliveries!!\n")
size=input("Enter the size of pizza you want S= small ,M= Medium, L= large\n")
bill=0
if size =="S" :
    bill =15
if size =="M" :
    bill=20
if size =="L" :
    bill=25
pepperoni=input("Press Y or N to add Pepperoni\n")
if pepperoni =="Y" :
    if size=="S" :
        bill+=2
    if size=="M" or size=="L" :
        bill+=3
cheese=input("Press Y or N to add extra cheese\n")
if cheese=="Y" :
    bill+=1
print(f"Your Final Bill is {bill}\n")
