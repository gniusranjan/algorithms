new=input()
j=new.split(' ')
i=int(j[0])
v=0
m=[]
while(v<i):
    x=input()
    m.append(x)
    v=v+1
#print(m)
l=int(input())
p=[]
a=0
while(a<i):
    pq= m[a].split(' ')
    p.append(pq)
    a=a+1
#print(m)
n=[]
for b in p:
    n.append(int(b[l]))
#print(n)
n.sort()
#print('answer')

for y in n:
    k=0
    for x in p:
        if int(x[l])==y:
            print(m[k])
        k=k+1