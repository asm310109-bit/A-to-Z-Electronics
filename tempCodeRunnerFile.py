a=input("enter your name")
for i in range(1,4):
    print(a)

a=input("enter your name")
b=int(input("enter your num"))   
for i  in range (0,b) :
    for x in a:
        print(x)

a=input("enter your name")
b=int(input("enter your num"))
for i in range(0,b):
    for k in a:
        print(k)
 
a=int(input("enter your num"))
for i in range(50,a,-1):
        print(i)

a=input("enter your name")
b=int(input("enter your num"))
if b<10:
    for i in range(0,b):
        print(a)
else:
    for w in range(1,4):
        print("too high")

a=int(input(" how many people invited in a party"))
if a<10:
    for i in range(0,a):
        b=input("ask for the name")
        print( b,"has been invited")
else:
    print("too many people")

                                                  #     NEW          #
a=input("enter your  fav colour")
for i in range(0,4):
    print(a)

a=int(input("enter your num"))
for i in range(1,a+1):
    print(i ,"square =" ,i*i)


b=int(input("enter your num"))
for i in range(1,b+1):
    print(i ,"Cube =" ,i*i*i)

a=input("enter your name")
for i in range(len(a)):
    print(a[i],"-",i + 1)

tab= int(input("enter a num between 1 to 15:-"))
for i in range(1,10):
    print(tab,"x",i,"=",tab*i)

num=int(input("enter your numer below hundred"))
for i in range(100,num-1,-1):
    print(i)

