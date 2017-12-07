'''
a=input('daaal be ').split()
b=input('aur daaal ').split()
A=[int(x) for x in a]
B=[int(x) for x in b]
def merge(a,b):
    x=i=j=0
    c=[]
    A.append(10000000)
    B.append(10000000)
    while x<len(a)+len(b)-2:
        if A[i] < B[j]:
            c.append(A[i])
            i=i+1
        else:
            c.append(B[j])
            j=j+1
        x=x+1
    A.pop()
    B.pop()
    return(c)
g=merge(A,B)
f=merge(A,B)
print(merge(A,B))

'''
#heap sort
def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


print(msort([7,5,3,9,1,8,4,6,2]))