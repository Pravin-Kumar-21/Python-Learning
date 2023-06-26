#BMI CALCULATOR

h=float (input("Enter Your Height in Meters\n"))
w=float (input("Enter Your Weiht in kg\n"))
bmi=int(w/(h*h))
print(bmi,"\n")
if bmi<=18.5 :
    print("Underweight\n")
elif bmi>18.5 and bmi <=25 :
    print("Normal Weight\n")
elif bmi>25 and bmi<=30 :
    print("Overweight\n")
else :
    print("Obese\n")
