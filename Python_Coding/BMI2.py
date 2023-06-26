height=float(input("Enter the height in meters\n"))
weight=float(input("Enter the Weight in kg\n"))
bmi=round(weight/(height**2),2)
if bmi<=18.5 :
    print(f"Your bmi is {bmi}, you are underweight\n")
elif bmi<=25 :
    print(f"Your bmi is {bmi}, you have normal weight\n")
elif bmi<=30 :
    print(f"Your bmi is {bmi}, You are slightly Obese\n")
else :
    print(f"Your bmi is {bmi}, You are clicnically Obese\n ")
