x=int(input());
y=int(input());
a=1;
b=0;
t=1;
n= int(input("Enter the number of terms to print"));
print("\t",b);
print("\t",a);
while n!=0:
    print("\t",t);
    b=a;
    t=a+b;
    a=t;
    n--;
    
