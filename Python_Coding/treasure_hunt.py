row1=["O","O","O"]
row2=["O","O","O"]
row3=["O","O","O"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=int(input("Where do you want to put the treasure?\n"))
ones=int(position%10)
tens=int(position/10)
tens-=1
if ones==1:
    row1[tens]="X"
if ones==2 :
    row2[tens]="X"
if ones==3 :
    row3[tens]="X"
print(f"{row1}\n{row2}\n{row3}")

