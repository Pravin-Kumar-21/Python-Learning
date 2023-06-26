#Program created to rando,ly select a user to pay the bill
import random
name=input("Enter Name of all People Separated comma and space\n")
new_list=name.split(',')
payer=new_list[random.randint(0,(len(new_list)-1))]
print(f"The bill will be payed by {payer}\n")
