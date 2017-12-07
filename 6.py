'''
def solve( A):
    a = []
    #A = list(A)
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            a.append(A[i] - A[j])
    a.sort()
    aa = list(set(a))
    b = []
    for i in aa:
        b.append(a.count(i))
    return (max(b) + 1)
'''"""
d={0:(0),1:(1),2:('a','b','c'),3:('d','e','f'),4:('g','h','i'),5:('j','k','l'),6:('m','n','o'),7:('p','q','r','s'),8:('t','u','v'),9:('w','x','y','z')}
l=[2,4,5]
i=0
an=set()
x=[0]*len(l)
def recur(l,i):
    if i==len(l):
        an.add(tuple(x))
    else:
        for j in d[l[i]]:
            x[i]=j
            i=i+1
            recur(l,i)
            i=i-1
recur(l,i)
print(an)
print(len(an))
nl=[]
for k in an:
    kk=''.join(k)
    nl.append(kk)
nl.sort()
print(nl)
"""
def Pa(A):
    a = int(A)
    l = []
    an = set()
    def para():
        if len(l)==2*a:
            an.add(tuple(l))
        elif sum(l)*2>len(l):
            l.append(0)
            para()
            del l[-1]
            if sum(l)<a:
                l.append(1)
                para()
                del l[-1]
        elif sum(l)*2 -len(l) == 0:
            l.append(1)
            para()
            del l[-1]
    para()
    ans = []
    for i in an:
        t = []
        for j in i:
            if j == 1:
                t.append('(')
            elif j == 0:
                t.append(')')
        tt = ''.join(t)
        ans.append(tt)
    return (ans)

print(Pa(3))


























