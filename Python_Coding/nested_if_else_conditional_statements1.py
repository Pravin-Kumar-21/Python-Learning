print("Wlecome to the roller coaster !!\n")
height= int(input("Enter your height in cm ?\n"))
if height>120 :
    print("You can Enjoy the Roller Coaster Ride \n")
    age=int(input("Enter Your age\n"))
    if age<=12 :
        print(" Do you want photos ?\n")
        s=input()
        if s=="yes" :
            print("You need to pay $8\n")
        else :
            print("You need to pay $5\n")
            
    elif age>12 and age<=18 :
        print("Do you want photos ?\n")
        s=input()
        if s=="yes" :
            print("You need to pay $11\n")
        else :
            print("You need to pay $7\n")
            
    elif age>18 and age<45 :
        print("Do you want photos ?\n")
        s=input()
        if s=="yes" :
            print("You need to pay $15\n")
        else :
            print("You need to pay $12\n")
    elif age>=45 and age<=55 :
        print("You dont need to pay any $ ")
else :
    print("You need to grow taller before you can enjoy this Ride\n")
