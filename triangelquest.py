#n=input()
bstr=input()
blist=bstr.split(' ')
a=0
b=0
c=0
d=0
e=0
for i in blist:
    if int(i)==1:
        a=a+1
    elif int(i)==2:
        b=b+1
    elif int(i)== 3:
        c = c + 1
    elif int(i)== 4:
        d = d + 1
    elif int(i)== 5:
        e=e+1
total=max(a,b,c,d,e)
if a==total:
    print(1)
elif b==total:
    print(2)
elif c==total:
    print(3)
elif d==total:
    print(4)
elif e == total:
    print(5)

#print(blist)
print(total)