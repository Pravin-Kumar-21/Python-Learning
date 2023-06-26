# Love Calculator using Python
print("Welcome to the Love Calculator!!!\n")
user1=input("Enter Your Name \n")
user2=input("Enter Your Beloved Name\n")
user1_lower=user1.lower()
user2_lower=user2.lower()
t=user1_lower.count("t")+user1_lower.count("r")+user1_lower.count("u")+user1_lower.count("e")+user2_lower.count("t")+user2_lower.count("r")+user2_lower.count("u")+user2_lower.count("e")
l=user1_lower.count("l")+user1_lower.count("o")+user1_lower.count("v")+user1_lower.count("e")+user2_lower.count("l")+user2_lower.count("o")+user2_lower.count("v")+user2_lower.count("e")
t=str(t)
l=str(l)
s=t+l
s=int(s)
if s<10 or s>90 :
    print(f"Your Score is {s}, You go together like coke and mentos\n")
elif s>=40 and s<=50 :
    print(f"Your score is {s}, You both are alright together\n")
else :
    print(f"Your score is {s}\n")

