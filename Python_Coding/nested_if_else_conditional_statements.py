print("Wlecome to the roller coaster !!\n")
height= int(input("Enter your height in cm ?\n"))
if height>120 :
    print("You can Enjoy the Roller Coaster Ride \n")
    age=int(input("Enter Your age\n"))
    if age<=12 :
        print("You need to pay $5\n")
    elif age>12 and age<=18 :
        print("You need to pay $7\n")
    else
        print("You need to pay $12\n")
else :
    print("You need to grow taller before you can enjoy this Ride\n")
