import random
name=input("Enter Name of all People Separated comma and space\n")
payer=name.split(',')
payer=random.choice(payer)
print(f"The is to be payed by {payer}")
