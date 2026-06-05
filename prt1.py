for i in range(45,51):
    print('info')

for i in reversed(range(4,9)) :
    print(i)   

l=4
while l<=10:
    print('desk')
    l+=2

p=10
while p>=4:
    print(p)
    p-=1

for i in range(1,10):
    if i==3:
        break
    print(i)

for i in range(782,786):
    if i ==784:
        continue
    print(i)

def info():
    a=3
    b=6
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
info()
 
def tiger(w,e):
    print(w+e)
    print(w-e)
    print(w*e)
    print(w/e)
tiger (6,2)

n= lambda a,b:a+b/5
print(n(4,5))

