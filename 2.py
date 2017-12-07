def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

A=[ 1, 2, 3 ]
def kth(n,k):
    if len(l)<no:
        a=int((k-1)/factorial(n-1))
        l.append(r[a])
        del r[a]
        k=k-a*factorial(n-1)
        n=n-1
        kth(n,k)
    #else:
        #return(''.join(map(str,l)))
no=len(A)
x=[]

for i in range(1,factorial(no)+1):
    l=[]
    r = list(A)
    #print(r)
    kth(no,i)
    x.append(l)
    #del l[:]

print(x)