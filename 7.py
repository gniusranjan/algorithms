#merge sort
c=input('enter the array to be sorted :').split(" ")
n=len(c)
C=[int(x) for x in c]
def merge(a,b):
    x=i=j=0
    c = []
    a.append(10000000)
    b.append(10000000)
    while x<len(a)+len(b)-2:
        if a[i] < b[j]:
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
        x=x+1
    a.pop()
    b.pop()
    return(c)

t=i=0
while (n>t):
    t=2**i
    i=i+1
j=k=0
while(k<2**(i-1)-len(c)):
     C.append(99999)
     k=k+1

while (j<i-1):

    d=[]
    if j==0:
        for x in range(1,int(len(C)/2)+1):
            a=[C[2*x-2]]
            b=[C[2*x-1]]
            d.append(merge(a,b))
    else:
        for x in range(1,int(len(C)/2)+1):
            a=C[2*x-2]
            b=C[2*x-1]
            d.append(merge(a,b))
    j=j+1
    C=d
print(C[0][:len(c)])