n =int(input())
i=0
total=0
while(i<=n):
    istr=str(i)
    b=0
    sum=0
    for a in istr:
        x=int(istr[b])
        sum=sum + x**2
        b=b+1
    root=sum**.5
    if root%1 ==0:
        total=total+i
    i=i+1
print(total)