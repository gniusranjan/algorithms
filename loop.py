from itertools import permutations as permu

n=int(input())
#b=0,c=0
l1=[]
for i in range(n):
    l1.append('a')

#b=0,c=1
l2=[]
for i in range(n-1):
    l2.append('a')
l2.append('c')

#b=0,c=2
l3=[]
for i in range(n-2):
    l3.append('a')
l3.append('c')
l3.append('c')

#b=1,c=1
l4=[]
for i in range(n-2):
    l4.append('a')
l4.append('c')
l4.append('b')

#b=1,c=0
l5=[]
for i in range(n-1):
    l5.append('a')
l5.append('b')

#b=1,c=2
l6=[]
for i in range(n-3):
    l6.append('a')
l6.append('c')
l6.append('c')
l6.append('b')

LL=[l1,l2,l3,l4,l5,l6]

y=0
for l in LL:
    x=list(permu(l))
    print(x)
    y=y+len(x)

print(y)