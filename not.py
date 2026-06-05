print("hello world")
print("Ahmed")

a=int(input("enter your 1 num"))
b=int(input("enter your 2 num"))
print(a+b)

num= int(input("enter your num"))
if num %2==0:
    print("Even")
else:
    print("Odd")

a=int(input("enter 1 num"))
b=int(input("enter 2 num"))
c=int(input("enter 3 num"))
if a>=b and a>=c:
    print("largest = ", a)
elif b>=a and b>=c:
    print("largest = ", b)
else:
    print("largest = ", c)


a=int(input("enter your 1 num"))
b=int(input("enter your 2 num"))
if a>=b:
    print("greater=",a)
else:
    print("greater= ",b)


a=int(input("enter your table number"))
for i in range(1,11):
    print(i,"x",a,"=",a*i)