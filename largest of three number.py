import sys
a=input("Give first number\t")
b=input("Give second number\t")
c=input("Give third number\t")
if(a>c) & (a>b):
    print("Biggest number is",a)
elif(c>a) & (c>b):
    print("Biggest number is",c)
else:
    print("Biggest number is",b)

