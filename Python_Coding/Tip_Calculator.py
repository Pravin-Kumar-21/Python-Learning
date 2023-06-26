print("Welcome to the Tip Calculator\n")
bill=float(input("What was the total bill\n"))
print("What percentage tip would you like to give ? 10,12 or 15\n")
tip=int(input())
head=int(input("How many people to split the bill ?\n"))
total=bill+(bill*tip/100)
total=total/head
print("Each person should pay ",round(total,2))
